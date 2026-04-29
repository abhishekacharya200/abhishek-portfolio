# Abhishek Acharya - Portfolio

Modern, animated portfolio showcasing Python, Django, and Full-Stack development projects.

[![CI](https://github.com/abhishekacharya200/abhishek-portfolio/actions/workflows/ci.yml/badge.svg)](https://github.com/abhishekacharya200/abhishek-portfolio/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Live:** [abhishek-portfolio-silk-six.vercel.app](https://abhishek-portfolio-silk-six.vercel.app)

## 🚀 Tech Stack

| Layer | Technology |
|-------|-----------|
| Framework | Next.js 15 (App Router) |
| Language | TypeScript 5 |
| Styling | Tailwind CSS 3 |
| Animations | Framer Motion 12 |
| Email | EmailJS |
| Icons | Lucide React |
| Deployment | Vercel |

## 🎯 Features

- Animated hero section with custom cursor
- Project showcase with case studies
- Animated skill progress bars
- Interactive timeline
- Contact form with EmailJS integration
- Fully responsive design
- GitHub contribution calendar

## 📋 Prerequisites

- [Node.js](https://nodejs.org/) v18 or later
- npm v9 or later (comes with Node.js)
- A free [EmailJS](https://www.emailjs.com/) account (for the contact form)

## 📦 Installation

```bash
# 1. Clone the repository
git clone https://github.com/abhishekacharya200/abhishek-portfolio.git
cd abhishek-portfolio

# 2. Install dependencies
npm install

# 3. Set up environment variables
cp .env.example .env.local
# Open .env.local and fill in your EmailJS credentials (see below)

# 4. Start the development server
npm run dev
``` 

Open [http://localhost:3000](http://localhost:3000) in your browser.

## 🔑 Environment Variables

Copy `.env.example` to `.env.local` and provide the following values:

| Variable | Description |
|----------|-------------|
| `NEXT_PUBLIC_EMAILJS_SERVICE_ID` | EmailJS service ID (found in your EmailJS dashboard) |
| `NEXT_PUBLIC_EMAILJS_TEMPLATE_ID` | EmailJS template ID for the contact form |
| `NEXT_PUBLIC_EMAILJS_PUBLIC_KEY` | EmailJS public (user) key |

### Getting EmailJS credentials

1. Create a free account at [emailjs.com](https://www.emailjs.com/).
2. Add an **Email Service** (e.g. Gmail) — copy the **Service ID**.
3. Create an **Email Template** — copy the **Template ID**.
4. Go to **Account → API Keys** — copy your **Public Key**.

## 🛠️ Available Scripts

```bash
npm run dev      # Start development server (http://localhost:3000)
npm run build    # Build for production
npm run start    # Start production server (run build first)
npm run lint     # Run ESLint
```

## 📁 Project Structure

```
abhishek-portfolio/
├── app/
│   ├── components/
│   │   ├── About/          # About section
│   │   ├── Contact/        # Contact form (EmailJS)
│   │   ├── Hero/           # Hero / landing section
│   │   ├── Navbar/         # Navigation bar
│   │   ├── Projects/       # Projects showcase
│   │   ├── Skills/         # Skills with progress bars
│   │   ├── Timeline/       # Experience / education timeline
│   │   ├── CustomCursor.tsx
│   │   └── ScrollProgress.tsx
│   ├── globals.css
│   ├── layout.tsx
│   └── page.tsx
├── data/
│   ├── projects.json       # Project entries
│   ├── skills.json         # Skills and proficiency levels
│   └── timeline.json       # Work / education history
├── lib/
│   └── constants.ts        # Site-wide constants
├── utils/
│   └── animations.ts       # Shared Framer Motion variants
├── public/                 # Static assets
├── .env.example            # Environment variable template
├── next.config.ts
├── tailwind.config.ts
└── tsconfig.json
```

## 🚀 Deployment

### Vercel (recommended)

1. Push your code to GitHub.
2. Import the repository at [vercel.com/new](https://vercel.com/new).
3. Add the three `NEXT_PUBLIC_EMAILJS_*` environment variables in the Vercel project settings.
4. Click **Deploy** — Vercel will automatically rebuild on every push to `main`.

### Other platforms (Netlify, Railway, etc.)

```bash
npm run build   # outputs to .next/
npm run start   # serves the production build
```

Set the same three environment variables in your platform's settings.

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 🔒 Security

Found a vulnerability? Please see [SECURITY.md](SECURITY.md) for the responsible disclosure process.

## 📄 License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.
