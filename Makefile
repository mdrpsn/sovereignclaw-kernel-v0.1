SHELL := /usr/bin/env bash
PY := python3

.PHONY: verify policy tests lint compile

verify: policy lint tests

policy:
	$(PY) -m tools.bootstrap_artifacts
	$(PY) -m tools.check_contract
	$(PY) -m tools.check_policy

lint:
	$(PY) -m compileall -q .

tests:
	$(PY) -m unittest -q

compile: policy lint tests
	$(PY) -m tools.gen_proof_packet
	$(PY) -m tools.append_audit
	$(PY) -m tools.check_policy
	@echo "Compile cycle artifacts written to proof/ and audit/."

.PHONY: handoff

handoff: compile
	@mkdir -p dist
	@tar -czf dist/handoff.tgz \
		docs/SAMPLE_HANDOFF_PACK.md \
		docs/OPERATOR_CHECKLIST.md \
		contracts/contract.json \
		policies/policy.json \
		policies/allowlist.skills.json \
		proof/PROOF_PACKET.md \
		audit/AUDIT_LOG.md
	@echo "Wrote dist/handoff.tgz"
