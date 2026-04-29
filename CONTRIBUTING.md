# Contributing to Abhishek Acharya's Portfolio

Thank you for your interest in contributing! Whether you're fixing a bug, improving the UI, or suggesting a feature, all contributions are welcome.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Commit Message Guidelines](#commit-message-guidelines)
- [Pull Request Process](#pull-request-process)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Features](#suggesting-features)

## Code of Conduct

Be respectful and constructive in all interactions. Harassment of any kind will not be tolerated.

## Getting Started

1. **Fork** the repository and clone your fork:

   ```bash
   git clone https://github.com/<your-username>/abhishek-portfolio.git
   cd abhishek-portfolio
   ```

2. **Install dependencies:**

   ```bash
   npm install
   ```

3. **Set up environment variables:**

   ```bash
   cp .env.example .env.local
   # Fill in your EmailJS credentials
   ```

4. **Create a feature branch:**

   ```bash
   git checkout -b feat/your-feature-name
   ```

5. **Start the dev server:**

   ```bash
   npm run dev
   ```

## Development Workflow

| Command | Purpose |
|---------|---------|
| `npm run dev` | Start the development server at `http://localhost:3000` |
| `npm run build` | Build for production (catches TypeScript/build errors) |
| `npm run lint` | Run ESLint across the codebase |

Before opening a pull request make sure both `npm run build` and `npm run lint` complete without errors.

## Commit Message Guidelines

Use the [Conventional Commits](https://www.conventionalcommits.org/) format:

```
<type>(<scope>): <short summary>
```

Common types:

| Type | When to use |
|------|-------------|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation only |
| `style` | Formatting, no logic change |
| `refactor` | Code restructure, no feature/fix |
| `chore` | Build process, dependency updates |

**Examples:**

```
feat(contact): add form validation feedback
fix(navbar): correct mobile menu close on route change
docs: update README with deployment instructions
```

## Pull Request Process

1. Ensure `npm run build` and `npm run lint` pass locally.
2. Update the README if your change affects setup, usage, or configuration.
3. Open a pull request against the `main` branch with a clear description of *what* changed and *why*.
4. The CI workflow will run lint and type-checking automatically — address any failures before requesting review.
5. A maintainer will review and merge or provide feedback.

## Reporting Bugs

Open a [GitHub Issue](https://github.com/abhishekacharya200/abhishek-portfolio/issues/new) with:

- A clear, descriptive title.
- Steps to reproduce the bug.
- Expected vs. actual behaviour.
- Browser / OS / Node version if relevant.
- Screenshots if applicable.

## Suggesting Features

Open a [GitHub Issue](https://github.com/abhishekacharya200/abhishek-portfolio/issues/new) with the `enhancement` label and describe:

- The problem you're trying to solve.
- Your proposed solution.
- Any alternatives you considered.
