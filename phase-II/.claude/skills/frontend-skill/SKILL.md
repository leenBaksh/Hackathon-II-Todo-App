---
name: frontend-skill
description: Build responsive web pages, create reusable components, implement layouts, and apply styling with modern CSS. Use for developing user interfaces and interactive web applications.
---

# Frontend Development

## Instructions

### 1. **Page Structure & Layout**
   - **Semantic HTML**: Use appropriate HTML5 semantic elements
   - **Responsive Design**: Implement mobile-first responsive layouts
   - **Grid & Flexbox**: Master CSS Grid and Flexbox for complex layouts
   - **Component Architecture**: Build reusable, modular components

### 2. **Component Development**
   - **Props/Attributes**: Design clear component interfaces
   - **State Management**: Handle component state and lifecycle
   - **Event Handling**: Implement user interactions
   - **Styling Approaches**: Choose between CSS modules, styled-components, or utility classes

### 3. **Styling & Design Systems**
   - **CSS Methodology**: Use BEM, SMACSS, or other naming conventions
   - **Design Tokens**: Define colors, typography, spacing as variables
   - **Animations**: Implement smooth transitions and micro-interactions
   - **Accessibility**: Ensure WCAG compliance and keyboard navigation

## Best Practices
- Follow mobile-first responsive design
- Optimize for performance (critical CSS, lazy loading)
- Ensure cross-browser compatibility
- Write accessible HTML (ARIA labels, semantic markup)
- Use CSS variables for theming
- Implement proper error boundaries and loading states
- Optimize images and assets
- Use proper font loading strategies
- Implement dark mode support

## Example Structures

### Page Layout with Semantic HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Modern Web Application</title>
    <meta name="description" content="A modern web application with responsive design">
    <link rel="stylesheet" href="styles/main.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
</head>
<body>
    <!-- Skip to main content for accessibility -->
    <a href="#main-content" class="skip-link">Skip to main content</a>
    
    <!-- Header with navigation -->
    <header class="header" role="banner">
        <div class="container">
            <nav class="navbar" aria-label="Main navigation">
                <a href="/" class="logo" aria-label="Homepage">
                    <svg class="logo-icon" width="40" height="40" aria-hidden="true">
                        <!-- Logo SVG -->
                    </svg>
                    <span class="logo-text">MyApp</span>
                </a>
                
                <!-- Mobile menu toggle -->
                <button class="menu-toggle" aria-label="Toggle menu" aria-expanded="false">
                    <span class="hamburger"></span>
                </button>
                
                <!-- Navigation links -->
                <ul class="nav-list">
                    <li><a href="/features" class="nav-link">Features</a></li>
                    <li><a href="/pricing" class="nav-link">Pricing</a></li>
                    <li><a href="/about" class="nav-link">About</a></li>
                    <li><a href="/contact" class="nav-link">Contact</a></li>
                </ul>
                
                <!-- Call to action -->
                <div class="nav-actions">
                    <button class="btn btn-secondary">Sign In</button>
                    <button class="btn btn-primary">Get Started</button>
                </div>
            </nav>
        </div>
    </header>
    
    <!-- Main content -->
    <main id="main-content" class="main">
        <!-- Hero Section -->
        <section class="hero" aria-labelledby="hero-heading">
            <div class="container">
                <div class="hero-grid">
                    <div class="hero-content">
                        <h1 id="hero-heading" class="hero-title">
                            Build Amazing Digital Experiences
                        </h1>
                        <p class="hero-description">
                            A powerful platform to create, manage, and scale your web applications 
                            with modern tools and best practices.
                        </p>
                        <div class="hero-actions">
                            <button class="btn btn-primary btn-large">
                                Start Free Trial
                            </button>
                            <button class="btn btn-outline">
                                Watch Demo
                            </button>
                        </div>
                        <div class="hero-stats">
                            <div class="stat">
                                <span class="stat-number">10K+</span>
                                <span class="stat-label">Active Users</span>
                            </div>
                            <div class="stat">
                                <span class="stat-number">99.9%</span>
                                <span class="stat-label">Uptime</span>
                            </div>
                        </div>
                    </div>
                    <div class="hero-visual">
                        <div class="dashboard-preview">
                            <!-- Dashboard illustration -->
                        </div>
                    </div>
                </div>
            </div>
        </section>
        
        <!-- Features Section -->
        <section class="features" aria-labelledby="features-heading">
            <div class="container">
                <h2 id="features-heading" class="section-title">Why Choose Our Platform</h2>
                <div class="features-grid">
                    <article class="feature-card">
                        <div class="feature-icon" aria-hidden="true">⚡</div>
                        <h3 class="feature-title">Lightning Fast</h3>
                        <p class="feature-description">
                            Optimized performance with code splitting and lazy loading.
                        </p>
                    </article>
                    <article class="feature-card">
                        <div class="feature-icon" aria-hidden="true">🔒</div>
                        <h3 class="feature-title">Secure by Design</h3>
                        <p class="feature-description">
                            Built with security best practices and regular updates.
                        </p>
                    </article>
                    <article class="feature-card">
                        <div class="feature-icon" aria-hidden="true">📱</div>
                        <h3 class="feature-title">Fully Responsive</h3>
                        <p class="feature-description">
                            Seamless experience across all devices and screen sizes.
                        </p>
                    </article>
                </div>
            </div>
        </section>
        
        <!-- FAQ Section -->
        <section class="faq" aria-labelledby="faq-heading">
            <div class="container">
                <h2 id="faq-heading" class="section-title">Frequently Asked Questions</h2>
                <div class="faq-list">
                    <details class="faq-item">
                        <summary class="faq-question">
                            Is there a free trial available?
                        </summary>
                        <div class="faq-answer">
                            <p>Yes, we offer a 14-day free trial with full access to all features.</p>
                        </div>
                    </details>
                    <details class="faq-item">
                        <summary class="faq-question">
                            Can I cancel my subscription anytime?
                        </summary>
                        <div class="faq-answer">
                            <p>Absolutely! You can cancel your subscription at any time with no hidden fees.</p>
                        </div>
                    </details>
                </div>
            </div>
        </section>
    </main>
    
    <!-- Footer -->
    <footer class="footer" role="contentinfo">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-brand">
                    <a href="/" class="logo">MyApp</a>
                    <p class="footer-tagline">
                        Building the future of web development.
                    </p>
                </div>
                <nav class="footer-nav" aria-label="Footer navigation">
                    <div class="footer-nav-section">
                        <h4 class="footer-nav-title">Product</h4>
                        <ul>
                            <li><a href="/features">Features</a></li>
                            <li><a href="/pricing">Pricing</a></li>
                            <li><a href="/api">API</a></li>
                        </ul>
                    </div>
                    <div class="footer-nav-section">
                        <h4 class="footer-nav-title">Company</h4>
                        <ul>
                            <li><a href="/about">About</a></li>
                            <li><a href="/blog">Blog</a></li>
                            <li><a href="/careers">Careers</a></li>
                        </ul>
                    </div>
                </nav>
            </div>
            <div class="footer-bottom">
                <p class="copyright">&copy; 2024 MyApp. All rights reserved.</p>
                <div class="footer-links">
                    <a href="/privacy">Privacy Policy</a>
                    <a href="/terms">Terms of Service</a>
                </div>
            </div>
        </div>
    </footer>
    
    <script src="scripts/main.js" defer></script>
</body>
</html>
