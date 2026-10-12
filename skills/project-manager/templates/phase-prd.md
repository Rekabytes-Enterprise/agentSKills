# Phase {{PHASE_ID}} PRD — {{PHASE_NAME}}

> Authoring note: Create one document per phase. Expand each requirement enough to implement and verify it. Repeat requirement/task entries as needed; all progress starts unchecked. Remove this note and all placeholders.

## 1. Document control

- Revision: {{PHASE_PRD_REVISION}}
- Status: Draft / awaiting document approval
- Product / implementation / acceptance owners: {{OWNERS_OR_UNASSIGNED}}
- Last updated: {{ACTUAL_DATE}}
- Approved proposal baseline: {{PROPOSAL_REVISION}}
- [Master PRD]({{MASTER_PRD_LINK}}) · [Development index]({{INDEX_LINK}}) · [Phase UAT plan]({{UAT_LINK}})
- Phase PRD/UAT approval: Pending

## 2. Objective, scope, and outcomes

Explain the user-visible or independently testable outcome, why this phase exists, deliverables, included master requirement IDs, and explicit exclusions. Describe how this phase fits the preceding/following phases and what can be demonstrated at its end.

## 3. Readiness and dependencies

- [ ] Phase PRD and UAT plan explicitly approved
- [ ] Required prior-phase outcomes accepted, or approved dependency exception recorded
- [ ] Blocking scope/technology decisions resolved
- [ ] Required interfaces, environment, accounts, and data available
- [ ] Acceptance owner and tester requirements agreed

List concrete dependencies, owners, evidence, and blockers. A separate explicit implementation request is still required; this checklist is not permission to start work.

## 4. Detailed phase requirements

### P{{PHASE_ID}}-REQ-{{NUMBER}} — {{REQUIREMENT_NAME}}

- Master traceability: {{FR_OR_NFR_IDS}}
- Priority / intended role / user outcome: {{PRIORITY_ROLE_OUTCOME}}
- Behavior and business rules: {{SPECIFICATION}}
- Inputs, validation, outputs, state transitions: {{DATA_AND_STATES}}
- UX: loading, empty, success, failure/recovery, accessibility: {{UX_EXPECTATIONS}}
- Permissions, sensitive data, abuse/security considerations: {{SECURITY_EXPECTATIONS}}
- Dependencies / integration contracts: {{DEPENDENCIES}}
- Acceptance criteria: {{GIVEN_WHEN_THEN_OR_EQUIVALENT}}
- UAT cases: {{P_PHASE_UAT_IDS_OR_REVIEWED_TECHNICAL_EXCEPTION}}
- Technical verification, where needed: {{METHOD_AND_EXPECTED_RESULT}}

## 5. Phase design and implementation plan

Describe relevant modules/screens, data entities/schema changes, API contracts, integration boundaries, migration/backward compatibility, deployment/configuration implications, and the ordered approach. Reference agreed architecture rather than introducing an unapproved stack.

- [ ] {{TASK_ID}} — {{BOUNDED_TASK}}; depends on {{DEPENDENCY_OR_NONE}}; verification {{METHOD}}; evidence pending

Separate implementation tasks from requirements and acceptance tests. Identify rollback/recovery and operational checks for this phase where applicable. Do not claim that a plan has been executed.

## 6. Requirement verification tracker

- [ ] P{{PHASE_ID}}-REQ-{{NUMBER}} — {{SHORT_REQUIREMENT}}; status: Not started; implementation evidence: None; linked UAT: {{UAT_IDS}}; acceptance: Pending

Repeat for every phase requirement. Check a requirement only after implementation and technical verification are evidenced; UAT acceptance remains separate. Label blocked/in-progress states in text and keep evidence attributable.

## 7. UAT and phase acceptance

Describe the required scenarios, tester/role coverage, critical business flows, environment/build, blocking defects, and authorized acceptance owner. Link all acceptance criteria to the companion UAT plan. Define any permitted defect waivers before using them; a waiver must record the owner's approval, rationale, and residual risk.

## 8. Risks and open decisions

| Risk / question | Impact | Action / mitigation | Owner | State / blocking? |
| --- | --- | --- | --- | --- |
| {{ITEM}} | {{IMPACT}} | {{ACTION}} | {{OWNER_OR_UNASSIGNED}} | {{STATE}} |

## 9. Completion and sign-off tracker

- [ ] Implementation requirements verified with evidence
- [ ] Relevant developer checks completed with recorded results
- [ ] UAT readiness confirmed and required cases executed
- [ ] Acceptance conditions satisfied; defects resolved/retested or explicit waivers approved
- [ ] Documentation, migration/release/rollback readiness complete where applicable
- [ ] Authorized reviewer accepted this phase/revision/build
- [ ] Master PRD and development index synchronized

Overall state: Not started  
Approval/implementation/UAT evidence: None recorded

| Event | Scope / revision / build | State | Owner / approver and actual date | Evidence |
| --- | --- | --- | --- | --- |
| Phase PRD and UAT plan approval | {{DOCUMENT_REVISIONS}} | Awaiting review | Pending | None |
| Phase acceptance | {{PHASE_SCOPE}} | Pending | Pending | None |
