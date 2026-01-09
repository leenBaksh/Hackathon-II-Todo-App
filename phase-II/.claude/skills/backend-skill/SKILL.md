---
name: backend-skill
description: Create RESTful APIs, handle HTTP requests/responses, implement middleware, and connect to databases. Use for building server-side applications and APIs.
---

# Backend API Development

## Instructions

### 1. **Route Structure & Organization**
   - **RESTful Design**: Follow REST conventions for endpoints
   - **Route Groups**: Organize related routes (users, products, orders)
   - **Versioning**: Implement API versioning (v1, v2)
   - **Resource Naming**: Use plural nouns for resource endpoints

### 2. **Request/Response Handling**
   - **Input Validation**: Validate all incoming data
   - **Error Handling**: Consistent error responses with proper HTTP status codes
   - **Response Format**: Standardized JSON response structure
   - **Middleware**: Implement authentication, logging, and rate limiting

### 3. **Database Integration**
   - **Connection Management**: Handle DB connections efficiently
   - **ORM/Query Builders**: Use abstractions for database operations
   - **Transactions**: Implement atomic operations for data integrity
   - **Connection Pooling**: Optimize database connections

## Best Practices
- Use environment variables for configuration
- Implement proper error handling and logging
- Add input validation for all endpoints
- Use middleware for cross-cutting concerns
- Implement rate limiting to prevent abuse
- Add comprehensive API documentation
- Use async/await for asynchronous operations
- Implement proper CORS configuration
- Add health check endpoints

## Example Structures

### Express.js Server Setup
```javascript
// server.js
const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const morgan = require('morgan');
const rateLimit = require('express-rate-limit');
const { connectDB } = require('./config/database');

const app = express();
const PORT = process.env.PORT || 3000;

// Security middleware
app.use(helmet());
app.use(cors({
  origin: process.env.ALLOWED_ORIGINS?.split(',') || ['http://localhost:3000'],
  credentials: true
}));

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // Limit each IP to 100 requests per windowMs
  message: 'Too many requests from this IP, please try again later.'
});
app.use('/api/', limiter);

// Body parsing
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Logging
app.use(morgan('combined'));

// Routes
app.use('/api/v1/auth', require('./routes/auth.routes'));
app.use('/api/v1/users', require('./routes/user.routes'));
app.use('/api/v1/products', require('./routes/product.routes'));

// Health check
app.get('/health', (req, res) => {
  res.status(200).json({
    status: 'OK',
    timestamp: new Date().toISOString(),
    uptime: process.uptime()
  });
});

// 404 handler
app.use('*', (req, res) => {
  res.status(404).json({
    success: false,
    error: 'Endpoint not found',
    path: req.originalUrl
  });
});

// Global error handler
app.use((err, req, res, next) => {
  console.error('Error:', err.stack);
  
  const statusCode = err.statusCode || 500;
  const message = err.message || 'Internal server error';
  
  res.status(statusCode).json({
    success: false,
    error: message,
    ...(process.env.NODE_ENV === 'development' && { stack: err.stack })
  });
});

// Connect to database and start server
connectDB()
  .then(() => {
    app.listen(PORT, () => {
      console.log(`Server running on port ${PORT}`);
    });
  })
  .catch((err) => {
    console.error('Failed to connect to database:', err);
    process.exit(1);
  });
