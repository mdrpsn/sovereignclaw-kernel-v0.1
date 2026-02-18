# Operator Checklist (SovereignClaw v0.1)

## Pre-flight
- Repo root opened in VS Code (WSL)
- make and python3 available
- contracts/contract.json validates

## Gates
- make verify passes
- policy gate passes
- unit tests pass

## Receipts
- proof/PROOF_PACKET.md generated
- audit/AUDIT_LOG.md appended

## Skill governance
- policies/allowlist.skills.json reviewed and pinned

## Handoff
- docs/SAMPLE_HANDOFF_PACK.md present
- dist/handoff.tgz created

## Client boundary
- No public exposure
- No unvetted skills/plugins
- No secrets in prompts or logs
