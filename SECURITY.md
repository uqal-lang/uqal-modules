# Security Policy

## Scope

This policy covers the `uqal-modules` repository — community and standard module implementations.

For vulnerabilities in the UQAL core engine, please report to the
[uqal-core repository](https://github.com/uqal-lang/uqal-core/security/advisories/new).

## Reporting a Vulnerability

**Do not open a public GitHub issue for security vulnerabilities.**

Use GitHub's private vulnerability reporting instead:
**[Report a vulnerability](https://github.com/uqal-lang/uqal-modules/security/advisories/new)**

Please include:
- The affected module name (e.g. `community.postgis`)
- A description of the vulnerability
- Steps to reproduce
- Potential impact
- A suggested fix if you have one

We will respond within **72 hours** and aim to release a patched version within **14 days** depending on severity.

## What counts as a vulnerability

- A module that generates unsafe queries (SQL injection, Cypher injection, etc.)
- A `native_validator.py` that fails to block destructive commands
- A connection module that leaks credentials or ignores TLS settings
- Any other issue that could compromise a user's database
