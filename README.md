# SovereignClaw v0.1 Kernel

A **Verified Shipping Kernel** you can drop into any repo.

**Guarantee**: no change is accepted unless it has a **contract**, passes **verification**, generates a **proof packet**, and writes an **audit entry**.

This v0.1 version is **stdlib-only** (no pip dependencies) so it runs in locked-down environments.

## Quick start

- Verify gates: `make verify`
- Generate artifacts: `make compile`

## What this enforces

- **Contract-first**: `contracts/contract.json` must exist and validate.
- **Policy gate**: `policies/policy.json` is evaluated (hard/soft rules).
- **Verification**: stdlib checks + unit tests must pass.
- **Receipts**: proof packet + append-only audit log.



