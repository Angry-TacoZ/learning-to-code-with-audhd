# Learning to code with AuDHD: product and engineering plan

Status: review draft based on the planning conversation through September 13, 2026. Repository publication and review workflow updated September 26, 2026. Product and architecture questions remain open; this is not a decision-complete implementation specification.

## 1. Purpose and success

Teach people to understand, direct, review, and troubleshoot agent-written software without requiring memorization of every piece of syntax. James is the first learner; an invited adult group is the initial audience. Other learners are welcome, but autism and ADHD needs guide the design.

The central analogy is hardware troubleshooting: identify parts, understand responsibilities and connections, follow evidence, and diagnose failure. Producing a working application is a motivating context, not sufficient evidence of learning.

A learner should eventually be able to:

- Map a feature across interface, browser code, server, database, and external services.
- Trace an action from input through processing to its result; locate the relevant code.
- Explain unfamiliar code using references, without recalling every syntax rule.
- Spot unsupported agent claims, investigate likely failure points, and choose a useful test.
- Recognize trust boundaries, including why private credentials cannot be shipped to a browser.
- Compare plausible stacks using workload, runtime behavior, ecosystem, maintainability, cost, and team constraints.
- Explain a design choice and its alternatives, including in an interview, without inventing the original author's rationale.

Do not declare older material obsolete merely because AI writes code. Prioritize foundational knowledge needed for oversight; reduce rote syntax drills. Evaluate learning claims rather than promising clinical or universal neurodivergent benefits.

## 2. Established requirements and boundaries

Established by James:

- Version one focuses on websites and web applications with an interactive preview.
- Offer selectable starting levels: complete beginner, beginner using agents, and some coding experience. Do not lock learners permanently to their initial choice.
- Learners choose from supported templates; James suggested around ten eventually, including a video game, news crawler, and online portfolio. Exact launch count and template list remain open.
- Let learners influence their project's idea and features within the supported learning experience.
- Use prepared lessons and scenarios for templates. Do not require AI to invent curriculum from arbitrary prompts.
- Provide a split workspace: agent and learning tasks on the left, running preview on the right.
- Teach the mechanisms behind choices and outcomes, not slogans such as a language always being faster or better.
- Make next steps and evidence of knowledge easy to find.
- Provide simple secure authentication, protected storage, understandable sharing controls, and easy reporting of bugs or incorrect learning content.
- Keep a decision journal suitable for a later portfolio artifact, explicitly crediting James's AuDHD-informed reasoning.
- Make implementation manageable for GPT-5.6 Luna-level agents through bounded tasks and verification.

Still open: live AI, actual local development versus browser-contained execution, stack, spending limits, authentication provider, launch template count, and initial lesson sequence. No unrestricted app generator, public enrollment, minors, payments, social feed, or arbitrary cloud-resource creation is included in this draft's proposed first release.

## 3. Learning experience

### Entry and return

Proposed flow: view a concrete project payoff, select starting experience, choose a supported project, select its initial feature, and enter the workspace. Keep required choices short. Evaluate whether a guest sample before authentication helps; persistence and account boundaries must be clear.

On return, show the exact saved activity, why it matters to the project, the last observation, and one next action. Let learners change direction without discarding work. Show saving, saved, offline, and failed-save states truthfully.

Do not impose a fixed session length. Provide meaningful small stopping points and optional depth. No punitive streaks, overdue lessons, forced countdowns, or claims that a short session indicates poor performance. Let learners pause and revisit explanations.

### Workspace

- Left: a clear current task, optional agent conversation, and contextual inspection tools for code, diffs, a component map, and checks. Open the relevant tool when needed rather than displaying every panel simultaneously.
- Right: a real interactive project preview with loading, build-error, stopped, and recovery states. A preview must not falsely appear current after a failed build.
- Connect visible behavior to the exact file, function, request, or data boundary responsible. Define unfamiliar technology names where used.
- Preserve preview interaction while allowing focus on a small code excerpt. Offer the full file as an optional expansion.
- Support resizable panes, keyboard controls, a single-pane focus mode, and sequential panels on narrow screens. Desktop is the proposed primary building environment; mobile reading/resumption is a proposed secondary target.
- Use calm visual hierarchy, readable contrast, clear labels, reduced-motion support, adjustable text, and predictable navigation. Avoid a diagnostic questionnaire as a prerequisite for personalization.

Accessibility target: WCAG 2.2 AA for the platform interface, with cognitive-accessibility guidance informing clear steps and personalization. Verify keyboard navigation, focus visibility, modal containment and restoration, zoom, screen-reader names, error announcements, and motion preferences. These checks do not establish that the product meets every learner's needs.

### Lesson structure

Each authored lesson has a practical payoff and follows the relevant portion of: locate -> trace -> explain -> investigate -> verify. Avoid making bug hunting the entry point before teaching the system model.

Proposed lesson package:

- Stable identifier, content version, prerequisites, supported template/features, learning objective, and optional depth.
- Reviewed explanatory content, initial project snapshot, allowed actions, and expected next states.
- Relevant component-map connections and code anchors tied to that snapshot.
- Exercises, hints, evaluation criteria, known misconceptions, and a recovery/reset path.
- A clear account of which facts the checks can establish and which judgments remain open.

Separate shared concepts from template-specific examples. Do not promise arbitrary combinations: explicitly author and test each supported feature path. Around ten templates should be an expansion target until authoring and maintenance costs are measured.

### Proposed pilot lessons

Use a portfolio/contact-form project as a candidate first vertical slice, subject to James's review:

1. Map the page, event handler, server boundary, and external service.
2. Trace a submit action; distinguish a visible success message from an actual successful request.
3. Find a fake private credential in a prepared example and explain why its location is unsafe. Use only synthetic credentials and mock services.
4. Inspect a small correction, observe success and failure behavior, and explain the evidence.
5. Compare two reasonable implementations against explicit requirements.

This candidate addresses James's experience with exposed credentials and false confidence in generated code. It is not a finalized course order.

Later runtime lessons can compare equivalent programs, including TypeScript/Node.js and Rust, using measured data representation, runtime overhead, allocation, and workload. Record environment and methodology; do not repeat social-media performance claims without evidence or compare unlike workloads.

### Knowledge and assessment

Use a visible skill map with evidence states such as not explored, practiced with help, demonstrated, and revisit suggested. Completion alone does not prove mastery; confidence is self-report, separate from demonstrated ability.

Use deterministic checks for structured decisions, code behavior, and known scenario states. Accept multiple authored valid answers. Do not score unrestricted prose by keyword presence or present unassessed writing as correct.

Free-text explanations can be saved for self-review against an authored rubric or human review. If automated semantic assessment is adopted later, evaluate it separately and display uncertainty. A learner can dispute any assessment through the reporting flow.

Include transfer exercises with unfamiliar code or changed constraints. Assess whether learners can explain and diagnose without repeating the exact training example. Track use of hints without punishment. Proposed pilot evidence: independent identification of a trust boundary, a plausible diagnosis with a test, and a stack tradeoff explanation on a second example.

## 4. Architecture decisions and feasibility gates

### Distinguish three systems

1. The learning platform: accounts, navigation, content, progress, reports, and administrative review.
2. The project runtime: files, build/run lifecycle, preview, and execution limits.
3. Evaluation and optional agent execution: reviewed checks and, only if selected, model-generated changes.

Application code authored by learners or agents is untrusted. It must not run inside the platform API process or receive the platform's credentials. Avoid microservices beyond a boundary required for execution safety or a demonstrated tooling need.

### Runtime options to test before choosing

| Option | Advantages | Constraints to investigate |
| --- | --- | --- |
| In-browser runtime, such as WebContainers | Actual Node.js project execution and embedded preview without local installation | Browser compatibility, cross-origin isolation, persistence, runtime scope, licensing, network restrictions |
| Local companion plus development server | Real local files and a broader language/toolchain path | Installation, permissions, updates, loopback access, authenticated commands, cross-platform support |
| Remote isolated workspace | Controlled environment and broader runtime options without local setup | Hosting cost, tenant isolation, lifecycle cleanup, resource abuse, network egress |

A preview iframe is only a display surface; it does not manage files or start a local server. WebContainers provides an in-browser Node.js runtime, not general support for Python, Rust, or arbitrary cloud services. Do not confuse the platform's backend language with the learner runtime.

Prototype one prepared project change and one deliberate failure, then reset and resume it. Inspect real browser output and console errors. Test supported browsers, isolated preview behavior, asset loading, reload, and interrupted execution. Record installation friction, compatibility, and costs. Choose a runtime only after evidence and James's preference.

### Stack candidates, not selections

- React + TypeScript for the interactive interface, with either a TypeScript backend or a bounded Python/FastAPI backend. Compare one-language simplicity against concrete Python evaluation-library benefits.
- Firebase or PostgreSQL/Supabase as managed auth/data candidates. Compare access-rule design, relational needs, local testing, deployment, export/deletion, and predictable cost before selection.
- Python does not make free-form meaning deterministic. Add it because demonstrated implementation needs justify the additional language and integration, not because prompt interpretation becomes rule-based.
- Do not add Rust, Go, or C to the platform merely because they are lesson subjects. Technology comparisons can initially use authored examples or controlled benchmark artifacts.

Write a short architecture decision record after each choice: requirements, options, evidence, tradeoffs, chosen approach, and conditions for reconsideration. James chooses technologies with at least two project-specific options explained.

### Stable module contracts

Specify language-appropriate types only after selecting the stack. Preserve these boundaries:

- Curriculum loader: returns a validated, versioned template/lesson package.
- Project runtime adapter: open snapshot, apply permitted change, run, report status, provide preview address, reset, stop. UI does not depend directly on a vendor runtime.
- Evaluator: receives exercise version and permitted answer/project evidence; returns pass/fail/needs-review plus reasons and hints. It cannot publish lessons or run unrestricted code in the platform backend.
- Progress store: account-scoped checkpoints and skill evidence referencing lesson versions. Checkpoints tolerate retries without duplicating awards or reverting newer progress.
- Report service: creates a private report tied to content/build/exercise versions and permits authorized review/status updates.
- Optional agent adapter: produces proposed changes and execution status; no direct access to production users or infrastructure.

Keep records minimal: user preferences, project/checkpoint, attempt/evidence, versioned curriculum, and reports. Define ownership, retention, and schema migrations before persistence implementation. Keep private evaluator answers out of ordinary client payloads when assessment integrity matters; server results still cannot prove ownership of untrusted browser execution.

## 5. Live AI evaluation, separate from authored teaching

James originally asked to test whether live AI is needed later. Preserve that gate.

Compare two implementations of the same authored lesson:

- Prepared agent steps and code patches that cause real project changes, clearly labeled as a guided scenario.
- A live agent constrained to the same project and objective, if James approves provider and budget.

Measure learner agency, comprehension and transfer, time to useful feedback, errors, recovery effort, latency, and cost. Use reviewed lesson content in both. The decision is not whether to let AI generate an entire curriculum.

If no live AI: UI must not suggest unrestricted instructions are understood. Free-form idea capture can coexist with clear supported choices, but text capture does not imply semantic execution.

If live AI: define context minimization, consent for provider sharing, provider retention terms, per-user quotas, application-level spending limits, timeouts, cancellation, patch review, rollback, and adversarial prompt/code tests before integration. Budget alerts alone are not a hard spending cap. No paid feasibility run is authorized by this planning document.

## 6. Security, privacy, and reporting

### Accounts and storage

- Proposed first release: invite-only adults, managed authentication, no custom password system. Choose email-link or federated sign-in with James; require stronger authentication for administrators where supported.
- Enforce ownership and authorization on every protected request or database rule, not only in UI navigation. Default deny and test user A against user B's identifiers.
- Separate admin and learner permissions; verify invite enforcement server-side.
- Use encrypted transport, managed encrypted storage, environment-separated credentials, and deployment secrets outside source control. Browser configuration must contain no private API credentials.
- Apply relevant session, CSRF, redirect, and recovery protections for the selected auth model. Render learner text safely; validate input and bound report/upload sizes.

### Untrusted project boundary

- Preview on an isolated origin/context with explicit sandbox permissions. Do not expose platform cookies, storage, secrets, or administrative endpoints to project code.
- Validate cross-window message origins, senders, and payloads. Do not weaken embedding or isolation settings merely to make a demo work.
- Limit execution lifetime, CPU/memory where the chosen runtime allows, dependencies, and network access. Prove the available controls; never claim a browser runtime automatically prevents all malicious behavior.
- For remote execution, deny private-network and metadata-service access and clean up workspaces. For local execution, use narrowly scoped authenticated commands, bounded workspace paths, and an explicit trust model before enabling process control.
- Use mock APIs in early lessons. A news crawler introduces external-fetching and SSRF concerns; it must use approved fixtures/sources until a separate safe-fetch design is reviewed.
- Do not run arbitrary learner code in the trusted evaluator service. Authored deterministic fixtures can execute in controlled jobs; arbitrary evaluation needs its own isolation.

### User control

Proposed defaults: private projects/progress, no public learner profiles, no advertising trackers, and optional analytics off. Essential account storage must be distinguished from optional external sharing; an online service cannot truthfully promise no processing anywhere.

Provide account export, deletion, and an understandable data/settings page. Explain mandatory hosting/auth processors and any optional AI processor. Define retention for attempts, reports, operational logs, and backups before the pilot; test deletion and explain backup expiry rather than promising instant removal from all backups.

Do not collect diagnoses or medication information to use the app. James approved an explicit AuDHD portfolio narrative; this is not blanket authorization to publish every personal detail from the conversation.

### Report and correction workflow

Every lesson and evaluation result has an easy Report issue action: software bug, wording, wrong answer, accessibility, or other. Prefill lesson/exercise/build versions and location; let users inspect the payload before submission. Do not silently attach source, screenshots, full conversations, personal data, or secrets.

Store reports privately with acknowledgement, status, and an admin queue. Suggested statuses: submitted, triaged, investigating, fixed, or closed with reason. Make repeated submissions safe and rate-limit abuse. Reviewers can reproduce against the recorded version, publish a correction through a PR, and flag affected lesson evidence for re-review without silently deleting learning history.

Critical security or incorrect-content incidents must have a way to disable the affected lesson/agent feature, revoke credentials if necessary, and communicate relevant remediation. A public GitHub issue must contain only an explicitly reviewed, sanitized reproduction.

Use OWASP ASVS as a scoped control checklist; record tested controls and gaps instead of claiming certification.

## 7. Repository and GitHub workflow

Repository setup, September 26, 2026: James authorized a public portfolio repository at [Angry-TacoZ/learning-to-code-with-audhd](https://github.com/Angry-TacoZ/learning-to-code-with-audhd). A minimal overview starts main; the planning documents and repository contribution guidance are reviewed on codex/project-plan. The initial CI check covers documentation and file hygiene only. Application checks and deployment remain future work.

Before implementation:

- Public repository ownership and visibility are established. Keep main as the default branch and review changes through PRs. Licensing remains open; do not assume a license grant from public visibility. Review future publication for private data and unsupported claims.
- Keep one repository initially. Proposed layout: apps/web, optional services/evaluator, shared contracts, curriculum, tests, and docs. Omit unused service directories rather than scaffolding speculative infrastructure.
- The planning PR adds root agent guidance, contribution/security instructions, a PR template, and a documentation check; the baseline has an ignore file. Add application setup/troubleshooting, .env.example placeholders, and issue templates when their concrete requirements are known.
- Keep generated output, dependency directories, user data, credentials, and private exports out of Git. Track dependency lockfiles and reviewed curriculum fixtures.
- Use codex/<short-purpose> branches and small cohesive PRs. Each substantial change links to an issue stating the learner problem, acceptance criteria, exclusions, and dependencies.
- PRs explain behavior, reasoning, risks, evidence, and journal/architecture updates where relevant. Never treat screenshots alone as proof of security or tests alone as proof of usability.

Require passing CI, resolved review comments, and review of the latest diff. Disable direct/force pushes to main when the account's available controls permit it. Verify GitHub plan support first: protected branches are not universally available on free private repositories. If unavailable, document the manual gap and let James choose a supported repository/account arrangement; do not buy an upgrade or imply enforcement exists.

For a solo repository, do not require an impossible self-approval. Record an independent agent review and James's merge decision; use a distinct authorized reviewer when available. Agent review comments are not automatically equivalent to GitHub approving-review enforcement. Security/runtime/authentication changes need a deliberate second review before release, with no unresolved blocking findings.

## 8. Building reliably with Luna-level agents

Do not assume a model is reliable merely because a task sounds small. Establish capability empirically against representative tasks.

Each implementation task must contain:

1. One observable outcome and its approved reference/fixture.
2. Exact relevant files and interfaces, plus permitted edit boundaries.
3. Inputs, outputs, failure behavior, and acceptance examples.
4. Existing commands to run and evidence to return.
5. Explicit exclusions and a stop condition for missing contracts, conflicting requirements, or security uncertainty.

Sequence work so UI fixtures, schemas, and adapters are agreed before integration. Supply a correct representative example. Split tasks by independently testable behavior, not arbitrary line count. Agents must inspect related callers, types, tests, and runtime effects; they must not make architectural choices to fill a gap.

Proposed benchmark tasks: render one lesson from a fixture; implement a checkpoint using a supplied contract; fix a known report-submission bug. Record correctness, regressions, review corrections, attempts, and platform-provided usage when available. Never invent token costs or claim a fixed reasoning-effort multiplier.

Use Luna for tasks demonstrated to fit this process. Escalate architecture, auth, runtime isolation, ambiguous failures, and repeated unsuccessful corrections to a more capable reviewer within James's budget. An agent must not weaken tests or access controls to pass a task. A reviewer should assess requirements and adversarial cases, not only read the author's explanation.

Definition of done: requested behavior observed, appropriate checks pass, diff reviewed, no new secret exposure, relevant documentation updated, and remaining limitations stated. Update the journal only when a meaningful decision changes; do not create verbose entries for every mechanical edit.

## 9. Verification, CI/CD, and operations

### Test layers

- Unit/contract checks: curriculum validation, progress transitions, adapter outputs, report validation, and deterministic evaluator valid/invalid cases.
- Integration: authenticated ownership, invite/admin enforcement, save/resume, content version changes, report lifecycle, and account export/deletion.
- Browser: select level/template, perform an activity, inspect code, observe changed preview, trigger/fix a known failure, resume, and report a disputed answer.
- Accessibility: automated checks plus keyboard, focus, zoom, screen-reader, and reduced-motion inspection of the actual workspace.
- Security: secret scan, dependency review, authorization negatives, stored script injection, untrusted preview messaging, and runtime-boundary tests relevant to the selected implementation.
- Educational evaluation: reviewed fixtures, useful hint progression, alternate valid answers, misconception coverage, and novel transfer tasks. Keep correctness of the platform distinct from effectiveness of teaching.

Use appropriate tools after stack selection; likely candidates include TypeScript type checking, Vitest, Playwright, and axe, with pytest/Ruff only if Python is selected. Confirm actual tool configuration before naming commands in agent tickets.

### CI pipeline

On PRs: clean dependency installation from lockfiles; lint/type checks; unit/contracts; curriculum checks; secret scanning; dependency vulnerability review; production build; core browser journey. Block actionable high-severity issues; any exception has an owner, reason, and expiry. Run broader runtime/browser coverage before releases and after relevant changes.

Use least-privilege workflow permissions and pinned third-party actions. Untrusted PR code must not execute with production secrets. Make preview deployments isolated and disposable with synthetic data; clean them up after PR closure. The reviewed decision journal is intentionally public; private research notes and user records must stay outside public artifacts and deployments.

### Release flow

PR -> checks and review -> merge -> staging -> smoke test -> explicit production promotion for the invited pilot. Use the same tested artifact where supported. Select hosting and its credential model before implementing the workflow.

Separate development, staging, and production data/configuration. Test schema and curriculum migrations before promotion. Use compatible additive migrations where possible; retain rollback artifacts and record the deployed commit/content version. Test restore as well as backup creation. A rollback must account for data changes, not just old application code.

Monitor build/runtime failures, failed saves, authentication errors, report delivery, and optional agent spend without logging learner text or credentials. Define incident ownership, retention, and thresholds before the pilot. Provide disable controls for problematic lessons and optional AI. Run the key journey on the deployed site before claiming a release works.

## 10. Delivery sequence and gates

| Phase | Deliverable | Exit evidence |
| --- | --- | --- |
| 0: Resolve decisions | Runtime/stack/budget/content choices; threat model; GitHub setup plan | James reviews options; decision records identify constraints and accepted approach |
| 1: Feasibility | One actual project preview, prepared change, code inspection, reset/resume | Browser evidence; isolation limitations; cost/license findings; no unsupported runtime claims |
| 2: Local learning slice | One authored feature sequence and component map; guest/local progress | James can trace and explain the feature; failure and recovery verified |
| 3: Private platform | Managed auth, ownership, durable progress, reporting/admin, export/deletion | Cross-user negatives and full browser journey pass; backup/restore and privacy behavior checked |
| 4: Teaching pilot | Reviewed lessons, transfer exercise, neurodivergent usability sessions | Report whether payoff, starting, resumption, and comprehension worked; revise from observations |
| 5: Optional live-agent experiment | Same lesson with live versus prepared changes, only if approved | Evidence of added benefit versus cost/error/latency; recorded adoption or deferral decision |
| 6: Template expansion | Additional tested templates and supported feature paths | Each template meets the same content/runtime/security contract; maintainability assessed before growing toward ten |
| 7: Invited release | Production workflow, operational runbook, portfolio draft | Deployed journey verified; release/recovery evidence; James reviews public narrative |

Do not give a calendar estimate until launch scope and feasibility are established. Complete one reliable vertical slice before multiplying content.

## 11. Decision journal and portfolio evidence

Maintain docs/decision-journal.md from this conversation onward. Entries distinguish James's statements, agent proposals, decisions, and verified findings. Use exact quotes only when available; identify paraphrases. Preserve changed direction and mistakes rather than rewriting history to appear inevitable.

Subsequent meaningful entries include the trigger, options/tradeoffs, James's reasoning, status, evidence/PR references, and conditions for reconsideration. Architectural detail can live in separate decision records linked from the journal.

The eventual case study should show: problem, AuDHD-informed insights, scope decisions, real architecture rationale, agent task/review strategy, a concrete discovered defect, validation evidence, and what changed after testing. Distinguish shipped results from plans. James's diagnosis-related openness is confirmed; private anecdotes and other people's data still need editorial care. Keep the medication detail out of the public draft by default.

## 12. Questions for the next planning conversation

Ask these one at a time, in dependency order, when James requests more questions:

1. Should the first pilot use prepared agent changes, with live AI evaluated later, or must an agent respond live from the start?
2. Is a browser-contained project acceptable, or is having local project files and a local development server an essential learning outcome?
3. Which two or three templates and first practical feature should anchor the pilot? Is approximately ten a launch requirement or expansion goal?
4. What learner choices must be supported within each template, and what should happen to unsupported requests?
5. Which stack does James choose after the feasibility comparison, including whether Python earns its extra integration cost?
6. What are the monthly hosting/model budget, allowed providers, and acceptable installation/browser requirements?
7. Which sign-in method, repository license, and hosting/data region fit the pilot? GitHub visibility is already public.
8. What retention, optional analytics/sharing, and account-deletion expectations should become policy?
9. What visual references and sensory/presentation controls should guide the first UI prototype?
10. How should open-ended explanations be reviewed initially, and what evidence would convince James that his diagnostic understanding is improving?

## Sources checked during planning

These sources support implementation constraints, not a claim that the design has been validated. Recheck version-sensitive details when implementing.

- [WebContainers introduction](https://webcontainers.io/guides/introduction): in-browser Node.js runtime.
- [WebContainers quickstart](https://webcontainers.io/guides/quickstart): preview integration and cross-origin-isolation requirements.
- [WebContainers browser support](https://webcontainers.io/guides/browser-support): compatibility considerations.
- [WebContainers commercial usage](https://webcontainers.io/enterprise): production commercial licensing is a decision gate.
- [MDN iframe reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe): embedding and sandbox controls.
- [W3C cognitive accessibility supplemental guidance](https://www.w3.org/WAI/WCAG2/supplemental/): clear steps and adaptation guidance.
- [OWASP ASVS](https://github.com/owasp/asvs): verification framework for the security checklist.
- [OWASP authorization guidance](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html): trusted enforcement of access controls.
- [GitHub protected branches availability](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches): account/repository support must be verified.
