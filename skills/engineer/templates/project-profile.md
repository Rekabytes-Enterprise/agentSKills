# Engineer profile — {{PROJECT_NAME}}

> Authoring note: Save as `docs/development/engineer-profile.md` in the consuming project only after explicit approval. Fill every placeholder, remove this note, and use project-relative paths. This configures the engineer skill; it is not a PRD replacement or implementation authorization.

## 1. Identity, scope, and approval

- Profile revision: {{PROFILE_REVISION}}
- Status: Approved for the recorded configuration scope
- Application/package scope: {{APPLICATION_SCOPES}}
- Master PRD / phase / UAT baseline: {{PRD_AND_PHASE_PATHS_AND_REVISIONS}}
- Approved configuration proposal: {{PROPOSAL_REFERENCE_AND_SCOPE}}
- Approver and actual approval date/reference: {{ACTUAL_APPROVER_AND_EVIDENCE}}
- Research reviewed: {{ACTUAL_VERIFICATION_DATE_OR_NOT_RECORDED}}
- Implementation / installs / upgrades / deployment permission: Not implied; requires explicit scoped authorization

## 2. Actual stack and compatibility evidence

| Application / layer | Runtime/framework/view/build tool | Installed/resolved versions | Evidence path / official source | Verified or unresolved |
| --- | --- | --- | --- | --- |
| {{APPLICATION_AND_LAYER}} | {{STACK_DIMENSIONS}} | {{VERSIONS_OR_EXPLICIT_UNKNOWN}} | {{EVIDENCE}} | {{STATE}} |

Distinguish installed versions, approved-but-not-installed tools, and proposed upgrades. Record language/runtime, framework, rendering/view layer, build tool, database, auth, styling, motion, test tools, and deployment boundary as applicable. Do not fill every runtime with the same JavaScript library.

## 3. Approved engineering choices

| Concern / application scope | Selected approach | Reason and alternatives rejected | Version/runtime compatibility | Status: installed / approved proposal / not needed |
| --- | --- | --- | --- | --- |
| {{CONCERN}} | {{SELECTION}} | {{RATIONALE}} | {{COMPATIBILITY_EVIDENCE}} | {{INSTALLATION_STATE}} |

Include appropriate state/cache/forms, validation/types, error policy/adapters, auth enforcement, motion, testing, and operational tools. Explicitly list items not needed. Choosing a tool here does not install it or authorize upgrading another one.

## 4. State ownership map

| State / data | Owner and lifetime | API/mechanism | Persistence / invalidation / reset | Security and rendering notes |
| --- | --- | --- | --- | --- |
| {{STATE_KIND}} | {{LOCAL_URL_STORE_QUERY_SESSION_DATABASE_OWNER}} | {{APPROVED_NATIVE_API}} | {{LIFECYCLE}} | {{SSR_REQUEST_TENANT_CREDENTIAL_NOTES}} |

Describe temporary UI, URL/form, shared client, server-derived data, identity/session, and durable domain state as applicable. Keep secrets out of browser storage and request-specific authenticated data out of process-global stores. Do not duplicate server business data into a permanent UI source of truth.

## 5. Architecture and existing components to retain

Describe module ownership, route/view/component conventions, shared boundaries, API/wire contracts, auth/permissions, session entrypoints, and store/provider topology. Record real implementation paths. Explain any explicitly approved scoped departures; this profile does not authorize a wholesale refactor.

## 6. Surface-specific design and motion

| Surface | Approved existing benchmark or selected preset | Token/component/font/icon/motion source paths | Native rendering/styling approach | Constraints / approved deviations |
| --- | --- | --- | --- | --- |
| {{CLIENT_ADMIN_MARKETING_OR_OTHER}} | {{APPROVED_BENCHMARK}} | {{ACTUAL_PATHS_OR_APPROVED_PROPOSED_PATHS}} | {{COMPATIBLE_IMPLEMENTATION}} | {{DENSITY_TYPOGRAPHY_GEOMETRY_ACCESSIBILITY_RULES}} |

Keep client, admin, and marketing identities separate. For a selected Mokara-derived preset, record its palette/geometry/typography, shared shell/chrome, reduced-motion and excluded-element rules. If using existing project design instead, record the actual benchmark; do not silently apply the presets.

## 7. Errors, validation, and production boundaries

Describe transport/normalization/action/presentation adapters and distinct render-error boundaries; render boundaries do not replace async/action handling. Include safe messages, server codes/status, runtime/local validation, authorization checks, retry/idempotency/rollback, logging redaction, environment exposure, request/worker lifecycle, and migration/release ownership as relevant. Use real project contracts, not Mokara's file names or auth implementation. No secret values.

## 8. Verification and evidence plan

| Check / native command | Application scope | Source of command / permission | Expected evidence | Local versus CI/owner-owned |
| --- | --- | --- | --- | --- |
| {{CHECK}} | {{SCOPE}} | {{SCRIPT_CONFIG_OR_EXPLICIT_PERMISSION}} | {{RESULT_ARTIFACT}} | {{OWNER}} |

Use verified configured commands, not invented scripts. Record relevant static/type checks, lint/format, focused tests, build gates, visual viewport/accessibility checks, and UAT handoff. Owner-managed servers and live/production actions need explicit authorization. Blank result fields are not passes; checks not run remain unverified.

## 9. Open decisions, risks, and exceptions

| Item | Affected scope | Question / mitigation | Owner | Blocking or non-blocking / state |
| --- | --- | --- | --- | --- |
| {{ITEM_OR_NO_OPEN_ITEMS}} | {{SCOPE}} | {{ACTION}} | {{OWNER_OR_UNASSIGNED}} | {{STATE}} |

Unresolved blockers prevent affected work. Record only explicitly accepted non-blocking assumptions/exceptions; do not fabricate compatibility evidence or approval.

## 10. Refresh and decision record

Recheck this profile against the actual PRD, manifests/lockfiles, runtime packages, rendering, design, and deployment on each use. Material drift requires targeted research and user approval **before** updating configuration. CLI/library updates do not erase project choices; framework major upgrades need their own approval.

| Revision / decision | Changed scope and reason | Sources / compatibility evidence | Actual approver/date/reference |
| --- | --- | --- | --- |
| {{PROFILE_REVISION}} | {{APPROVED_CHANGE}} | {{EVIDENCE}} | {{ACTUAL_APPROVAL}} |

Next authorized action or pending user request: {{NEXT_ACTION_OR_AWAITING_IMPLEMENTATION_REQUEST}}
