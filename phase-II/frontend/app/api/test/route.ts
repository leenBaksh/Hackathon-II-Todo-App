// Next.js API route for testing purposes
// This is just a placeholder - in a real app, this would connect to your backend

export async function GET(request: Request) {
  return new Response(
    JSON.stringify({
      message: 'Frontend API is working!',
      timestamp: new Date().toISOString(),
      backendUrl: process.env.BACKEND_API_URL || 'Not set'
    }),
    {
      status: 200,
      headers: {
        'Content-Type': 'application/json',
      },
    }
  )
}