# Phase {{PHASE_ID}} UAT plan — {{PHASE_NAME}}

> Authoring note: Create one UAT plan per phase, with meaningful project-specific cases. A scenario is a test specification, not a result. Repeat cases, role coverage, and execution records as needed. Remove this note and all placeholders.

## 1. Document control and acceptance scope

- UAT plan revision: {{UAT_REVISION}}
- Status: Draft / awaiting document approval
- [Phase PRD]({{PHASE_PRD_LINK}}) · [Master PRD]({{MASTER_PRD_LINK}}) · [Development index]({{INDEX_LINK}})
- Included phase requirement IDs: {{PHASE_REQUIREMENT_IDS}}
- Exclusions / reviewed technical coverage exceptions: {{EXCLUSIONS_AND_JUSTIFICATIONS_OR_NONE}}
- UAT plan approval: Pending
- Execution state: Not run
- Acceptance authority: {{OWNER_OR_UNASSIGNED}}

## 2. Tester requirements and responsibilities

Specify the required tester personas/roles, domain knowledge, permissions, independence/review requirements where relevant, and who prepares data, executes cases, triages defects, retests, and signs off. A developer completing a task does not automatically accept their own work on the user's behalf.

| Tester persona / application role | Skills or business knowledge needed | Required access | Assigned person | Responsibility |
| --- | --- | --- | --- | --- |
| {{PERSONA_OR_ROLE}} | {{TESTER_REQUIREMENTS}} | {{PERMISSIONS}} | {{PERSON_OR_UNASSIGNED}} | {{RESPONSIBILITY}} |

## 3. Environment, accounts, and test data

- Approved test environment and exact build/revision: {{ENVIRONMENT_AND_BUILD_OR_PENDING}}
- URLs/endpoints, browser/device/OS coverage, feature flags/configuration names: {{TEST_CONFIGURATION}}
- Required accounts/roles and secure provisioning instructions: {{ACCOUNTS_WITHOUT_CREDENTIAL_VALUES}}
- Seeded/synthetic data and known starting state: {{DATA_AND_PREPARATION}}
- External services, sandbox modes, email delivery, and integration prerequisites: {{SERVICE_SETUP}}
- Reset/cleanup, retention, and evidence-storage location: {{CLEANUP_AND_EVIDENCE}}

Use synthetic or appropriately authorized data. Do not put passwords/tokens/private user data in this document or screenshots. Do not perform destructive actions, incur charges, or test production without explicit authorization; document required approvals for those scenarios.

## 4. Entry criteria

- [ ] Phase PRD and this UAT plan approved
- [ ] Required implementation and developer verification evidenced
- [ ] Test environment/build, integrations, accounts, and data ready
- [ ] Testers and acceptance authority assigned with required access
- [ ] Blocking dependencies and test-safety permissions resolved

If entry criteria fail, record UAT as Blocked or Not run, not Passed.

## 5. Requirements-to-test traceability

| Phase requirement | Master requirement | Acceptance criterion | UAT case IDs | Coverage notes |
| --- | --- | --- | --- | --- |
| P{{PHASE_ID}}-REQ-{{NUMBER}} | {{FR_OR_NFR_IDS}} | {{CRITERION}} | P{{PHASE_ID}}-UAT-{{CASE_NUMBER}} | {{NOTES}} |

Every in-scope acceptance criterion needs a test or an explicitly reviewed coverage exception with a separate verification method. Include relevant success, invalid/empty input, errors/recovery, unauthorized/role-isolation, and accessibility/device cases. Avoid unrelated boilerplate scenarios.

## 6. Executable UAT cases

### P{{PHASE_ID}}-UAT-{{CASE_NUMBER}} — {{SCENARIO_NAME}}

- Requirement(s) / acceptance criterion: {{REQUIREMENT_IDS_AND_CRITERION}}
- Type / business criticality: {{POSITIVE_NEGATIVE_PERMISSION_RECOVERY_ETC_AND_PRIORITY}}
- Tester persona / application role: {{TESTER_ROLE}}
- Preconditions and initial data: {{PRECONDITIONS}}

| Step | Tester action / exact input | Expected observable result |
| --- | --- | --- |
| 1 | {{ACTION}} | {{EXPECTED_RESULT}} |
| 2 | {{NEXT_ACTION}} | {{EXPECTED_RESULT}} |

- Final acceptance assertion: {{DECIDABLE_PASS_CONDITION}}
- Cleanup/reset: {{CLEANUP}}
- Evidence required: {{SCREENSHOT_LOG_EXPORT_OR_OTHER_SAFE_EVIDENCE}}
- Status: Not run
- Actual result: Not recorded
- Tester / executed date / build: Not recorded
- Evidence link(s): None
- Defect ID(s): None recorded

## 7. Execution and defect records

Append attributable execution/retest records without hiding earlier failures. Use `Not run`, `Passed`, `Failed`, or `Blocked`; only a recorded matching actual result can be Passed.

| Case ID | Attempt / build | Tester / actual date | Status | Actual result / evidence | Defect IDs |
| --- | --- | --- | --- | --- | --- |
| P{{PHASE_ID}}-UAT-{{CASE_NUMBER}} | Pending | Pending | Not run | None | None recorded |

| Defect ID | Linked case / requirement | Severity and user impact | Reproduction / evidence | Owner / state | Retest or waiver |
| --- | --- | --- | --- | --- | --- |
| {{DEFECT_ID_IF_ANY}} | {{LINKED_IDS}} | {{SEVERITY_AND_IMPACT}} | {{STEPS_AND_EVIDENCE}} | {{OWNER_AND_STATE}} | {{RESULT_OR_AUTHORIZED_WAIVER}} |

Agree severity, blocking thresholds, and which defects are non-waivable with the user. Non-waivable blockers must be resolved and retested before acceptance. Other waivers must be permitted by the agreed policy; record approvals with scope, rationale, owner, and residual risk. Failed cases remain Failed even if accepted with a waiver.

## 8. Exit criteria and acceptance tracker

- [ ] All required UAT cases executed with attributable results/evidence
- [ ] Acceptance criteria met, or explicitly approved exceptions/waivers documented
- [ ] Blocking defects resolved and retested, or policy-permitted waivers explicitly approved; no non-waivable blocker remains
- [ ] Remaining defects reviewed with approved disposition and residual risk
- [ ] Required tester-role/device coverage completed or approved coverage exception recorded
- [ ] Acceptance authority explicitly signed off on this phase/build
- [ ] Phase PRD, master PRD, and development index updated consistently

Acceptance decision: Pending  
Accepted scope/revision/build: Pending  
Authorized reviewer / actual date: Pending  
Sign-off evidence / approved exceptions: None recorded

If criteria are unmet, report the phase as Awaiting acceptance or Blocked. Test execution, implementation completion, and user acceptance are separate events.
