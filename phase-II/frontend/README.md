# Todo Frontend

This is the frontend for the Todo application, built with Next.js 14+ using the App Router.

## Getting Started

First, install the dependencies:

```bash
npm install
```

Then, run the development server:

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

## Environment Variables

Create a `.env.local` file in the root of the frontend directory to configure the backend API URL:

```env
BACKEND_API_URL=http://localhost:8000
```

## Project Structure

- `app/` - Contains the Next.js App Router pages
- `public/` - Static assets
- `components/` - Reusable React components
- `lib/` - Utility functions and constants

## Tech Stack

- Next.js 14+ (App Router)
- React 18+
- TypeScript
- Tailwind CSS (can be added later)