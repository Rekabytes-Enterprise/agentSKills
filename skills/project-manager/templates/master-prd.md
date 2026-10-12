# Product Requirements Document — {{PROJECT_NAME}}

> Authoring note: Expand every section with project-specific details. Repeat requirement, phase, risk, and decision entries as needed. Do not invent numeric targets, approvals, or test results. Remove this note and all placeholders.

## 1. Document control and approval

- PRD revision: {{PRD_REVISION}}
- Status: Draft / awaiting document approval
- Product owner / document owner: {{OWNERS_OR_UNASSIGNED}}
- Last updated: {{ACTUAL_DATE}}
- Planning proposal baseline: {{APPROVED_PROPOSAL_REVISION_AND_REFERENCE}}
- Approval to generate documents: {{ACTUAL_APPROVER_AND_SCOPE}}
- Approval of this PRD: Pending
- Related documents: [Development index]({{INDEX_LINK}}); {{PHASE_DOCUMENT_LINKS}}

## 2. Product context and success

Describe the problem, evidence/user need, product vision, value proposition, business/user outcomes, and how success will be evaluated. Separate launch acceptance from longer-term success metrics.

| Outcome / metric | Definition and measurement | Agreed target or decision needed | Owner |
| --- | --- | --- | --- |
| {{OUTCOME}} | {{MEASUREMENT}} | {{TARGET_OR_TBD}} | {{OWNER_OR_UNASSIGNED}} |

## 3. Users, roles, and journeys

Describe personas, access roles, important tasks, journey entry/exit points, prerequisites, and pain points. Include normal, empty, failure/recovery, and permission-denied paths where applicable. State device, accessibility, language, and connectivity needs.

## 4. Scope and prioritization

- In-scope MVP: {{MVP_SCOPE}}
- Later increments: {{LATER_SCOPE}}
- Explicitly out of scope: {{EXCLUSIONS}}
- Existing implementation to retain/adapt: {{CURRENT_STATE_AND_PATHS}}
- Prioritization method and rationale: {{PRIORITIES}}

## 5. Functional requirements

For every requirement, describe concrete behavior, roles, inputs/outputs, business rules, validation, error handling, dependencies, and measurable acceptance criteria. Do not substitute implementation tasks for user requirements.

### FR-{{REQUIREMENT_NUMBER}} — {{REQUIREMENT_NAME}}

- Priority and rationale: {{PRIORITY}}
- User story / outcome: {{USER_STORY}}
- Detailed behavior and rules: {{BEHAVIOR}}
- Boundary, error, and authorization behavior: {{EDGE_CASES}}
- Acceptance criteria: {{GIVEN_WHEN_THEN_OR_EQUIVALENT}}
- Assigned phase requirement(s): {{PHASE_REQUIREMENT_IDS_AND_LINKS}}
- UAT coverage: {{UAT_IDS_AND_LINKS_OR_JUSTIFIED_TECHNICAL_EXCEPTION}}

## 6. Non-functional requirements

Cover applicable performance, reliability, accessibility, compatibility, security, privacy, observability, maintainability, recovery, and data retention needs. Agree measurable targets and the environment/method that will verify them; list unresolved targets explicitly.

| ID | Requirement / rationale | Target | Verification method | Phase / coverage |
| --- | --- | --- | --- | --- |
| NFR-{{NUMBER}} | {{REQUIREMENT}} | {{AGREED_TARGET_OR_TBD}} | {{METHOD}} | {{PHASE_AND_TEST_IDS}} |

## 7. Approved architecture and technology decisions

Record the selected frontend/platform, backend/API boundaries, data/storage, authentication, hosting, and delivery/testing/operations choices. Explain fit to the draft, options considered, rejected tradeoffs, and what remains subject to confirmation. Add a component/data-flow diagram if it clarifies the design.

| Area | Selected approach | Reason and alternatives considered | Risks / evidence |
| --- | --- | --- | --- |
| {{AREA}} | {{SELECTION}} | {{PROJECT_SPECIFIC_RATIONALE}} | {{RISKS_AND_SOURCES}} |

## 8. Data and integrations

Describe key entities, relationships, ownership, lifecycle, validation, migration/import/export, and retention/deletion. Specify API/integration boundaries, contracts, error/retry behavior, concurrency/idempotency, rate limits, and external dependencies as relevant. Record sensitive-data handling without real personal data or secret values.

## 9. Authentication, authorization, and security

Describe identity flows and providers, session lifecycle, recovery/revocation, role/tenant permissions, server-side enforcement, audit needs, abuse controls, and account deletion where applicable. Include a role/action permission matrix when needed. For no-auth products, state the rationale and how privileged operations/data remain protected. Identify configuration variable names only.

## 10. Hosting, delivery, and operations

Explain managed/self-hosted/hybrid topology, environment separation, region/residency, deployment ownership, configuration/secrets, CI/release checks, migrations, health checks, logs/alerts, backup ownership, restore validation, rollback, and incident response. Include cost drivers and verified estimates or explicit unknowns. Do not equate selecting hosting with provisioning approval.

## 11. Phased delivery plan

| Phase | Testable outcome / deliverables | Master requirements | Dependencies / readiness | PRD / UAT |
| --- | --- | --- | --- | --- |
| {{PHASE_ID_AND_NAME}} | {{OUTCOME}} | {{FR_AND_NFR_IDS}} | {{DEPENDENCIES}} | {{LINKS}} |

Explain sequencing, any safe parallel work, release boundaries, and estimate assumptions. Do not promise dates without agreement.

### Phase {{PHASE_ID}} progress

- [ ] Phase PRD and UAT plan approved — evidence pending
- [ ] Readiness and dependencies confirmed — evidence pending
- [ ] Implementation requirements verified — evidence pending
- [ ] UAT results recorded — evidence pending
- [ ] Acceptance conditions satisfied; defects resolved or approved waivers recorded — evidence pending
- [ ] Authorized phase sign-off recorded — evidence pending

## 12. Validation and UAT strategy

Distinguish developer verification (unit/integration/build/security checks) from user acceptance. Specify who owns UAT, required environment/accounts/data, acceptance authority, and defect severity/waiver policy. Explain traceability from master requirement to phase requirement to UAT case, including technical coverage exceptions requiring review. Every phase must have a UAT plan; pending tests are not passing tests.

## 13. Risks, assumptions, dependencies, and open questions

| Item | Type | Impact / affected scope | Mitigation or decision question | Owner | State / blocks approval? |
| --- | --- | --- | --- | --- | --- |
| {{ITEM}} | {{TYPE}} | {{IMPACT}} | {{ACTION}} | {{OWNER_OR_UNASSIGNED}} | {{STATE}} |

## 14. Project completion and approval record

Define project-wide acceptance, migration/release/operational readiness, documentation/handoff, and unresolved-defect policy. Completion requires evidence and recorded authorization, not just checked tasks.

- [ ] Master PRD explicitly approved for this revision
- [ ] All required phase PRDs and UAT plans approved
- [ ] All required phases accepted with evidence
- [ ] Operational/release readiness reviewed where applicable
- [ ] Final project acceptance recorded

| Decision / approval / revision | Scope | State | Approver and actual date | Evidence / rationale |
| --- | --- | --- | --- | --- |
| Planning proposal {{PROPOSAL_REVISION}} | {{ACTUAL_APPROVED_SCOPE}} | Approved for document generation only | {{ACTUAL_APPROVER_AND_DATE_OR_DATE_NOT_RECORDED}} | {{REFERENCE}} |
| This master PRD {{PRD_REVISION}} | {{DOCUMENT_SCOPE}} | Awaiting review | Pending | None |

Changes to approved scope or architecture require discussion and change-proposal approval before revising the baseline; affected documents then require renewed approval.
