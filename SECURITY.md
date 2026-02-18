# Security Boundaries

**Default posture**: deny by default.

- No public endpoints by default.
- No unaudited third-party skills/plugins.
- No secrets in prompts, commits, or logs.
- Any new dependency must include an **unwind deadline**.

If you cannot describe the shutdown path, do not deploy.
