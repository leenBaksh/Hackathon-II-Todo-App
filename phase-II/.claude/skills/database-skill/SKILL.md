---
name: database-skill
description: Design database schemas, create tables, manage migrations, and optimize database structures. Use for relational and non-relational database implementations.
---

# Database Schema Design & Management

## Instructions

### 1. **Schema Design Principles**
   - **Normalization**: Follow 3NF to eliminate redundancy
   - **Relationships**: Define one-to-one, one-to-many, many-to-many relationships
   - **Indexing**: Identify columns for optimal indexing
   - **Constraints**: Implement proper data constraints and validation

### 2. **Table Creation & Structure**
   - **Primary Keys**: Always define primary keys
   - **Foreign Keys**: Establish proper referential integrity
   - **Data Types**: Choose appropriate data types for each column
   - **Default Values**: Set sensible default values where applicable
   - **Nullable/Not Null**: Define column nullability explicitly

### 3. **Migration Management**
   - **Version Control**: Track schema changes with migration files
   - **Rollback Support**: Ensure migrations can be rolled back safely
   - **Environment Consistency**: Maintain identical schemas across environments
   - **Migration Order**: Manage dependencies between migrations

## Best Practices
- Always use migrations for schema changes (never modify production directly)
- Add indexes for frequently queried columns
- Use meaningful table and column names
- Document complex relationships and business logic
- Consider partitioning for large tables
- Implement soft deletes instead of hard deletes
- Use ENUM types for fixed value sets
- Set up database backups and recovery procedures

## Example Structures

### SQL (PostgreSQL) Schema Example
```sql
-- users.sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    uuid UUID DEFAULT gen_random_uuid() UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    is_active BOOLEAN DEFAULT TRUE,
    email_verified BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP WITH TIME ZONE
);

-- Add indexes for performance
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_username ON users(username);
CREATE INDEX idx_users_created_at ON users(created_at);

-- Add check constraints
ALTER TABLE users ADD CONSTRAINT email_format_check 
    CHECK (email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$');
