# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| Latest (`main`) | ✅ |

## Reporting a Vulnerability

If you discover a security vulnerability in this project, **please do not open a public GitHub issue**.

Instead, report it privately by sending an email to:

**javascript1415@gmail.com**

Please include:

- A clear description of the vulnerability.
- Steps to reproduce or a proof-of-concept.
- The potential impact you see.
- Any suggested fix if you have one.

### What to expect

- An acknowledgement within **48 hours**.
- A status update within **7 days** (confirmed, need more info, or not a vulnerability).
- Credit in the fix commit/release notes if you wish.

## Scope

This is a personal portfolio site. The primary security-sensitive area is the **EmailJS contact form** (environment variables). Never commit `.env.local` or share your EmailJS credentials publicly.

## Out of Scope

- Issues in third-party dependencies — please report those upstream.
- UI/UX bugs that have no security impact — open a regular issue instead.
