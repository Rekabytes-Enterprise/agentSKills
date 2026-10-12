# Operator/admin design

Adapted from Mokara's editorial operator-console design. Keep the **inspect shared sources → preserve console identity/data → review all affected states** workflow. This guide is scoped to operator/admin UI, not the customer dashboard or public marketing.

## Inspect the actual benchmark

Read the approved PRD/design, shared styles/tokens, shell/navigation/auth screens, control/data renderers, font/asset loading, responsive rules, and security/CSP requirements. Record actual project-relative sources in the engineer profile. Reuse shared helpers instead of introducing parallel page styles.

Preserve the existing approved console identity. For a new console without one, propose the following Mokara-derived preset and get approval. Use the actual approved runtime: plain HTML/CSS/JS, Blade, Livewire, Vue, React, or another stack. The source console is not a reason to add React/Tailwind to a PHP/HTML app.

## Preserved editorial preset

- Typography: self-hosted Instrument Sans for content and IBM Plex Mono 400 for labels, navigation numbers, timestamps, and metadata. Retain font licenses and secure asset-loading/CSP constraints. Font acquisition or installation requires its own permission; these names are a design proposal, not bundled font assets.
- Weight: regular `400` for headings, metrics, navigation, table headers/links, controls, and badges; brand `500` is the established exception. Use size, spacing, contrast, and placement rather than unnecessary bold.
- Palette: cool gray background `#f4f5f5`, white panels, graphite `#232626`, muted `#636b6b`, burnt-orange accent `#a63e24`, subtle rules. Orange is a restrained navigation/state accent, not a page wash. Preserve semantic status colors.
- Geometry: `2px` panel / `4px` control radii, thin borders, and quiet surfaces. No heavy shadows, cream backgrounds, pill-shaped panels, or customer indigo glass styling.
- Composition: masthead, numbered console index, generous title area, ruled summary metric strip. Preserve useful asymmetric overview grids; group toolbar/data/pager into directory panels and related facts on detail pages. Auth/signed-out views use restrained centered cards.

Do not overwrite another approved admin identity with this preset. Record the selected benchmark and approved deviations per surface.

## Controls and operational data

Use shared actionable button styling for filters, clearing filters, refresh, details, paging, and sign-out. Preserve native semantics: buttons for actions, links for navigation, labeled forms, and keyboard-operable disclosures. Keep visible focus/hover/disabled/expanded states.

Preserve every existing field, support action, disclosure, filter, URL state, pagination, and refresh behavior. Distinguish zero, unavailable, stale, and error data honestly; no fake empty-success fallback. Styling changes must not alter plan grants, monitoring meaning, auth, or privileges.

Preserve HTML escaping, CSP, safe asset/font loading, and renderer data attributes where used. Keep operator presentation separate from backend/database/provider secrets. Do not copy a page-specific toolbar when a shared renderer owns it.

Motion stays short and restrained with reduced-motion alternatives. No WebGL or continuous decorative animation in the operations console; use the existing compatible native mechanism.

## Review

Follow the project's owner-managed server and verification rules. Review affected pages plus auth/signed-out, loading/empty/error, and disclosure states at narrow mobile widths and `1280/1440/1600/1920` desktops. Check long labels, table scrolling, wrapped filters, focus, and clear actions. Label fixture/sample data explicitly; it is not live verification.

Do not propagate console typography, orange palette, or squared geometry into the client. Marketing remains a separate surface with its own approved design.
