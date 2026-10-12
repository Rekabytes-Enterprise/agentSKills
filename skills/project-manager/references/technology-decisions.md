# Technology, hosting, and authentication decisions

Use this guide after understanding the user's draft and before requesting proposal approval. It is a discussion framework, not a prescribed stack.

## Start from constraints

Confirm product/platform, existing implementation, team experience, delivery priority, budget, expected traffic/storage, integrations, offline/realtime needs, sensitive data, residency/compliance, and operational capacity. Prefer retaining an adequate current stack over an unnecessary rewrite. For prototypes, distinguish what can be deferred from what would make production unsafe.

Compare two or three coherent end-to-end options. Each should identify frontend/client, backend boundaries, data store, authentication, file storage, hosting, delivery/testing, and operations where relevant. Explain what work a managed service removes and what still belongs to the application team. Do not silently equate lower infrastructure bills with lower total cost.

Examples to consider only when they fit:
- An existing framework with managed database/auth and managed application hosting for a small team prioritizing delivery.
- An application with an app-owned SQL database and Better Auth, on managed hosting or a self-hosted deployment when ownership/control matters.
- The current implementation with incremental improvements, or another ecosystem better suited to the team's platform and expertise.

Do not assume JavaScript, Next.js, a monorepo, containers, Supabase, or authentication are required for every project.

## Hosting comparison

| Dimension | Managed hosting / services | Self-hosted infrastructure |
| --- | --- | --- |
| Project fit | Useful when the team wants less infrastructure work | Useful when control, custom networking, residency, or existing ops expertise justify it |
| Responsibility | Provider manages defined platform layers; team still owns app security, configuration, data access, and incident coordination | Team owns patching, TLS, networking, uptime, observability, backups, restoration, scaling, and incident response |
| Cost drivers | Compute tiers, database/storage usage, bandwidth, seats, service-specific limits | Servers, storage, bandwidth, redundancy, backup systems, and operator time |
| Delivery | Often integrated builds/previews; check workload/runtime support | More deployment control; requires an explicit deployment and rollback process |
| Portability | Varies with proprietary features and data export options | Varies with deployment packaging and database/service dependencies; not automatically portable |

Consider a hybrid when useful: for example, a self-hosted app with a managed database. If proposing a VPS/container platform, identify who operates it and how backups are restored. If recommending managed hosting, identify runtime restrictions, regional availability, spend controls, and vendor failure/exit plans. For all options, plan staging, secrets, migrations, health checks, logs, and rollback.

Present actual costs only when verified from current authoritative sources for the user's expected usage, currency, and region. Otherwise provide cost drivers and explicitly labeled estimates/unknowns. Never promise that a free tier will cover production.

## Authentication comparison

First ask which flows are required: email/password, verification/recovery, magic links, social OAuth, MFA, enterprise SSO, organizations, mobile sessions, account deletion, and auditability. Separate **authentication** (who someone is) from **authorization** (what they may do).

| Option | What it is | When to consider it | Responsibilities / questions |
| --- | --- | --- | --- |
| Supabase Auth | An authentication service within the Supabase ecosystem, available through managed or self-hosted setups | Supabase is already used, or its backend integration fits the draft | Confirm session and server integration, authorized data access/RLS where used, email/OAuth setup, relevant plan limits, and the team's responsibilities for the selected hosting mode |
| Better Auth | An application-integrated authentication library, not a managed backend platform | The application needs app-owned auth/data and its runtime/database integration is suitable | Confirm adapters/plugins for required features, database/migrations, session security, email delivery, provider configuration, updates, and operating ownership |
| Other suitable solution | A managed identity provider or an established framework's auth solution | Enterprise identity requirements, existing team conventions, or a different ecosystem make it a better fit | Check required flows, user/machine pricing, data residency, export/migration, and operational responsibility |
| No authentication | Public/local use without identity requirements | The product does not need protected user data or identity | Confirm that removing auth does not leave privileged operations or private data exposed |

Compare the **actual required features**, not brand names. Do not attribute database, storage, or realtime features to Better Auth, or count all of Supabase's backend features as authentication features. Neither option automatically implements the project's role/tenant authorization model.

For the chosen option, specify protected routes/actions, session/cookie/token boundaries, server-side authorization, role/tenant isolation, recovery/revocation, rate limiting/abuse handling, secret management, and privacy/account deletion as applicable. Do not invent custom cryptography or security claims.

## Evidence and decision record

Use current authoritative documentation when tools/access permit. If browsing is unavailable, explicitly mark version-sensitive feature/price claims unverified and identify what needs checking; do not pretend research was performed. Record source URLs and access dates for verified vendor claims. No network writes, account creation, installs, or provisioning are needed for this comparison.

Finish with:
1. A comparison tied to the draft and constraints.
2. One recommendation and its rationale, disadvantages, and mitigations.
3. The user's selected option and what remains unresolved.
4. A clear approval question covering scope, stack, hosting, auth, and the phase outline.

If the user rejects the recommendation, discuss their preference and update the proposal. A recommendation is not a decision until approved.
