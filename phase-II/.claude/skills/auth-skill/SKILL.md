---
name: auth-skill
description: Implement authentication systems with signup, signin, password security, JWT tokens, and Better Auth integration. Use for web application authentication.
---

# Authentication System Implementation

## Instructions

### 1. **Core Authentication Flow**
   - Secure user registration with validation
   - Protected login with session management
   - Password hashing with bcrypt/Argon2
   - JWT token generation and verification

### 2. **Security Implementation**
   - Password hashing (salt + pepper)
   - JWT token refresh mechanism
   - Rate limiting on auth endpoints
   - CORS configuration for APIs

### 3. **Better Auth Integration**
   - OAuth provider configuration
   - Social login setup (Google, GitHub, etc.)
   - Session management with Redis
   - Multi-factor authentication

## Best Practices
- Never store plain-text passwords
- Use HTTPS in production
- Set secure HTTP-only cookies for tokens
- Implement proper error handling (don't reveal sensitive info)
- Validate all user input server-side
- Use environment variables for secrets
- Regular token rotation and expiration

## Example Structure

### JWT Authentication Middleware
```javascript
// middleware/auth.js
const jwt = require('jsonwebtoken');

const authenticateToken = (req, res, next) => {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];
  
  if (!token) return res.sendStatus(401);
  
  jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
    if (err) return res.sendStatus(403);
    req.user = user;
    next();
  });
};
