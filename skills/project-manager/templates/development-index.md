# Development plan — {{PROJECT_NAME}}

> Authoring note: Repeat the phase entry for every phase. Use paths relative to this generated README. Approval and implementation checks start unchecked. Remove this note and all placeholders.

Planning baseline: {{BASELINE_REVISION}}  
Overall status: Draft / awaiting document approval  
Product owner / acceptance authority: {{OWNER_OR_UNASSIGNED}}

## Document index

- [Master PRD]({{MASTER_PRD_LINK}})
- Phase {{PHASE_ID}} — {{PHASE_NAME}}: [PRD]({{PHASE_PRD_LINK}}) · [UAT plan]({{PHASE_UAT_LINK}})

## Master phase tracker

### Phase {{PHASE_ID}} — {{PHASE_NAME}}

Outcome: {{TESTABLE_OUTCOME}}  
Depends on: {{PHASE_DEPENDENCIES_OR_NONE}}  
Current status: Not started  
Evidence / blockers: None recorded

- [ ] Phase PRD and UAT plan explicitly approved — approver/revision/evidence pending
- [ ] Readiness and dependencies confirmed — evidence pending
- [ ] Implementation verified against phase requirements — evidence pending
- [ ] Required UAT executed and results recorded — evidence pending
- [ ] Acceptance criteria satisfied; defects resolved or explicitly waived — evidence pending
- [ ] Phase accepted by authorized reviewer — sign-off pending

## Tracking rules

`[ ]` means pending; `[x]` means completed with recorded evidence. Use text for `In progress`, `Blocked`, or `Awaiting review`. Documentation approval does not imply implementation completion; implementation does not imply UAT acceptance.

Update this index together with the master PRD, affected phase PRD, and UAT results. Include evidence paths and identify user-reported versus independently verified results. Keep failed cases visible even when a defect waiver is approved. Reopen affected checks on regression or scope change.

## Approval scope and pending decisions

| Decision / approval | Scope and revision | State | Owner / approver | Evidence |
| --- | --- | --- | --- | --- |
| Planning proposal | {{APPROVED_PROPOSAL_SCOPE}} | Approved to generate documents only | {{ACTUAL_APPROVER}} | {{ACTUAL_APPROVAL_REFERENCE}} |
| Generated PRDs and UAT plans | {{DOCUMENT_REVISIONS}} | Awaiting review | {{OWNER_OR_UNASSIGNED}} | None |
| {{OPEN_DECISION}} | {{AFFECTED_SCOPE}} | {{STATE}} | {{OWNER_OR_UNASSIGNED}} | {{EVIDENCE_OR_NONE}} |

## Next action

{{NEXT_REVIEW_OR_DECISION_NEEDED}}
