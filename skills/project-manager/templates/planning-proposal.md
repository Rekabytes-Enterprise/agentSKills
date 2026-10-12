# Planning proposal — {{PROJECT_NAME}}

> Authoring note: Present this proposal in conversation before creating PRD files. Fill the comparison with relevant options, not generic recommendations. Remove this note when presenting.

Revision: {{PROPOSAL_REVISION}}  
Status: Awaiting proposal approval

## 1. Draft and product understanding

- Problem and desired outcome: {{PROBLEM_AND_OUTCOME}}
- Users, roles, and primary journeys: {{USERS_AND_JOURNEYS}}
- Existing implementation inspected: {{FILES_AND_FINDINGS_OR_NO_IMPLEMENTATION}}
- Existing components to retain: {{RETAINED_COMPONENTS}}
- MVP scope: {{MVP_SCOPE}}
- Later scope / explicit exclusions: {{OUT_OF_SCOPE}}

## 2. Constraints and decisions to discuss

| Area | Confirmed constraint / preference | Missing decision or assumption | Decision owner |
| --- | --- | --- | --- |
| Platform, team, scale, budget, timeline | {{CONSTRAINTS}} | {{QUESTIONS}} | {{OWNER_OR_UNASSIGNED}} |
| Data, privacy, residency, integrations | {{DATA_CONSTRAINTS}} | {{DATA_QUESTIONS}} | {{OWNER_OR_UNASSIGNED}} |

## 3. Suitable stack options

| Dimension | Option A | Option B | Optional option C |
| --- | --- | --- | --- |
| Frontend/platform and backend | {{A_APP}} | {{B_APP}} | {{C_APP}} |
| Database and file storage | {{A_DATA}} | {{B_DATA}} | {{C_DATA}} |
| Authentication and authorization | {{A_AUTH}} | {{B_AUTH}} | {{C_AUTH}} |
| Hosting: managed/self-hosted/hybrid | {{A_HOSTING}} | {{B_HOSTING}} | {{C_HOSTING}} |
| Testing, delivery, monitoring, backups | {{A_OPERATIONS}} | {{B_OPERATIONS}} | {{C_OPERATIONS}} |
| Fit to this draft and retained code | {{A_FIT}} | {{B_FIT}} | {{C_FIT}} |
| Advantages | {{A_PROS}} | {{B_PROS}} | {{C_PROS}} |
| Disadvantages and material risks | {{A_CONS}} | {{B_CONS}} | {{C_CONS}} |
| Cost drivers and operating owner | {{A_COST_AND_OWNER}} | {{B_COST_AND_OWNER}} | {{C_COST_AND_OWNER}} |
| Migration / portability considerations | {{A_EXIT}} | {{B_EXIT}} | {{C_EXIT}} |

Recommendation: {{RECOMMENDED_OPTION_AND_PROJECT_SPECIFIC_REASON}}  
Tradeoffs and mitigations: {{TRADEOFFS_AND_MITIGATIONS}}  
User's selection, if discussed: {{SELECTED_OPTION_OR_PENDING}}  
Verified sources / unverified claims: {{SOURCES_AND_UNCERTAINTIES}}

## 4. Proposed phases

| Phase | User/testable outcome | Scope boundary | Dependencies | UAT focus |
| --- | --- | --- | --- | --- |
| {{PHASE_ID_AND_NAME}} | {{OUTCOME}} | {{BOUNDARY}} | {{DEPENDENCIES}} | {{UAT_FOCUS}} |

Repeat for all proposed phases. Explain release strategy, operational readiness, and which deliverables can be reviewed independently. Dates/estimates remain provisional unless agreed.

## 5. Risks and open decisions

| Risk / decision | Impact | Mitigation / question | Owner | Blocks proposal approval? |
| --- | --- | --- | --- | --- |
| {{RISK_OR_DECISION}} | {{IMPACT}} | {{ACTION}} | {{OWNER_OR_UNASSIGNED}} | {{YES_OR_NO}} |

## 6. Approval request — stop after asking

Please review this planning proposal: scope, stack, hosting, authentication, phase outline, and assumptions. Do you approve revision {{PROPOSAL_REVISION}} so I can create the master PRD, phase PRDs, and UAT plans in `docs/development/`, or should we revise it?

This approval permits documentation only. Generated documents will still require your review; implementation and deployment are not authorized.
