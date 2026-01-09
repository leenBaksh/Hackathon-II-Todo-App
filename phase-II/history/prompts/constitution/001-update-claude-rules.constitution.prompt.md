---
id: 1
title: Update CLAUDE.md with project requirements
stage: constitution
date: 2026-01-08
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: 1-console-todo
user: unknown
command: none
labels: [CLAUDE.md, configuration, agents, stack]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - /mnt/d/Phase-I-Hackathon-II/phase-II/CLAUDE.md
tests:
 - none
---

## Prompt

Update the claude.md file based on my project requirements. In this file:

Use Auth Agent for authentication
Use Frontend Agent for frontend development (e.g., Next.js)
Use DB Agent for database design and operations
Use Backend Agent for FastAPI development

Below are my project requirements:

"""
Basic Level Functionality
Objective: Using Claude Code and Spec-Kit Plus transform the console app into a modern multi-user web application with persistent storage.
💡Development Approach: Use the Agentic Dev Stack workflow: Write spec → Generate plan → Break into tasks → Implement via Claude Code. No manual coding allowed. We will review the process, prompts, and iterations to judge each phase and project.
Requirements
Implement all 5 Basic Level features as a web application
Create RESTful API endpoints
Build responsive frontend interface
Store data in Neon Serverless PostgreSQL database
Authentication – Implement user signup/signin using Better Auth
Technology Stack
Layer
Technology
Frontend
Next.js 16+ (App Router)
Backend
Python FastAPI
ORM
SQLModel
Database
Neon Serverless PostgreSQL
Spec-Driven
Claude Code + Spec-Kit Plus
Authentication
Better Auth

Better Auth can be configured to issue JWT (JSON Web Token) tokens when users log in. These tokens are self-contained credentials that include user information and can be verified by any service that knows the secret key.
How It Works
User logs in on Frontend → Better Auth creates a session and issues a JWT token
Frontend makes API call → Includes the JWT token in the Authorization: Bearer <token> header
Backend receives request → Extracts token from header, verifies signature using shared secret
Backend identifies user → Decodes token to get user ID, email, etc. and matches it with the user ID in the URL
Backend filters data → Returns only tasks belonging to that user

 """

## Response snapshot

Updated CLAUDE.md to incorporate the project's vision, technology stack (Next.js 16+, FastAPI, Neon PostgreSQL, Better Auth), and specialized agent mappings. Defined success criteria based on the SDD workflow and manual coding restrictions.

## Outcome

- ✅ Impact: Established project-specific guardrails and agent roles in CLAUDE.md.
- 🧪 Tests: n/a
- 📁 Files: CLAUDE.md updated.
- 🔁 Next prompts: Start creating feature specifications.
- 🧠 Reflection: CLAUDE.md now serves as an authoritative source for project-specific instructions and tool usage.

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): n/a
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): none
