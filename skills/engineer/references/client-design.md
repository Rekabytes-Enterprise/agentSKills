# Client/product design

Adapted from Mokara's signed-in client design. Keep the **inspect → extend → preserve interaction → review** workflow. Scope this guide to the customer/product UI, not the operator console or public marketing.

## Inspect the actual benchmark

Read the approved design/PRD and current neighboring components, global/token styles, app shell, shared page header, list/filter/chip controls, drawers, charts/settings/team views when relevant, and shared motion definitions. Record their real project-relative paths in the engineer profile. Supporting design prose can be stale; inspect the actual implementation and raise conflicts instead of silently replacing it.

An established approved project identity takes precedence. For a new UI without a benchmark, propose the following Mokara-derived client preset during onboarding and get approval before applying it. The preset is framework-neutral: implement its tokens with the approved CSS/component system, not a mandatory Next/Tailwind dependency.

## Preserved client preset

Identity: a calm, compact workspace with indigo accents, cool translucent surfaces, softly rounded controls, and restrained depth.

- Typography: a system font stack; compact task titles/navigation around `0.92rem` at 500, section labels commonly 600. Body/metadata are not blanket bold. Preserve purposeful brand emphasis; do not import the admin all-regular convention or marketing display headings.
- Palette: ink `#0f172a`, muted `#64748b`, indigo accent `#6366f1`, white surfaces at 0.72/0.55 opacity, soft slate borders, and a subtle cool gradient wash. Do not substitute admin orange, cream, or marketing navy sections.
- Geometry: card radius `18px`, buttons `11px`, icon controls `10px`, full-round chips where counterparts use them. Keep subtle shadows/glass blur; do not flatten into the admin's square ruled panels.
- Shell: `260px` desktop sidebar, `280px` mobile drawer, and `800px` breakpoint when this preset is adopted. One reusable page header; preserve its compact `0.92rem` text and size-8-equivalent notification control rather than copying chrome per page.
- Components: reuse the selected token source, card/field/button/pill recipes, and appropriately compact chip/icon primitives. Add genuinely shared new values centrally. Use Tailwind tokens only if the approved stack actually uses Tailwind; plain CSS or other native systems can implement the same recipe.

Do not copy these values over a different approved project's system. Record the selected benchmark/preset and any explicitly approved deviations in the profile.

## Composition and interaction

Preserve each page's useful composition: dense grouped task lists with filters/inline actions and drawers; chart-focused analytics; tile-based settings; layered/member team views when these exist. Consistency means shared chrome/tokens, not forcing every page into the same grid or oversized metric cards.

Reuse the approved icon system. The source preset uses hand-drawn SVG icons with accessible labels; keep route-private drawings local until genuinely shared. Avoid introducing a second icon library or emoji UI glyphs just to restyle a page.

Preserve keyboard interactions, focus, errors, loading/empty states, tour hooks where present, all fields/data, and enabled/disabled behavior. Intentionally inactive controls do not authorize new features.

Use shared motion timings/variants and approved native animation facilities. For a compatible React/Motion implementation, preserve presence-owned exits, `layout="position"` lists, and portal positions during exits; keep heatmap tracks/cells and compact ChipShell-like wrappers outside motion when using this preset. Respect reduced motion; decorative WebGL is not a default product addition.

## Review

Follow owner-managed server and permitted verification rules. Inspect authenticated UI in the browser when available and authorized; if redirected to login, use source evidence and report visual-review limits. Do not create accounts or fabricate signed-in verification.

Check narrow mobile widths and `1280/1440/1600/1920` desktops, overflow, long labels, contrast on composited translucent backgrounds, focus, controls, and reduced motion. Fix concrete accessibility defects while preserving the selected visual language. Do not propagate operator-console styling into the client; marketing has a separate approved benchmark.
