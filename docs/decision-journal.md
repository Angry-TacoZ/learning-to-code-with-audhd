# Decision journal

Initial planning session: September 13, 2026, with dated follow-up entries. Retrospective assembled from the planning conversation at James's request. Unless quotation marks are used, James's reasoning is paraphrased. Entries distinguish intent, proposals, and verified outcomes.

## 001 — Teach oversight of agent-written software

**James's reasoning:** Coding work increasingly involves agents. He wants to guide them, understand their output, and take responsibility for quality rather than learn on the assumption that humans will type every line.

**Status:** Established product purpose.

**Implication:** Prioritize reading, tracing, debugging, requirements, security, testing, and explanation. Reduce syntax memorization; do not discard foundations needed to judge code.

## 002 — Start privately, support different starting levels

**James's choice:** Begin with himself and invited adults. All three proposed experience levels should be selectable before lessons.

**Status:** Established. Specific diagnostic/onboarding behavior remains open.

**Implication:** Do not treat every learner as either a complete beginner or an experienced programmer. No public/minor launch scope is established.

## 003 — Engagement depends on value, not a fixed lesson duration

**James's reasoning:** The manageable investment depends on executive dysfunction, enjoyment, and whether the payoff is clear. A fixed short-lesson duration does not answer that design challenge.

**Status:** Established design priority. Specific interventions need testing.

**Agent proposals:** Show payoff early, allow a small entry action and optional depth, save exact progress, support returning, and avoid pressure mechanics. These are proposed responses, not claims that they work for all autistic or ADHD learners.

## 004 — Preserve a moment of interest

**James's example:** He began this project promptly after having the idea because he expected his likelihood of starting to fall if he delayed.

**Status:** Personal experience, approved as context for AuDHD-informed design; not a universal or medical claim.

**Implication:** Investigate low-friction entry, capturing intent, and restoring context after a break.

## 005 — Agency and visible change make the effort meaningful

**James's reasoning:** Ownership over the idea and features helps connect learning to value. Seeing changes in real time would encourage continued engagement.

**Status:** Established priorities.

**Implication:** Learners should influence their supported project and interact with the actual result. A completed lesson badge is not a substitute for observable cause and effect.

## 006 — Authored templates were James's proposed constraint

**James's reasoning:** A catalog of supported project templates can have prepared lessons and scenarios; AI need not invent the curriculum on demand. He described roughly ten possible templates, such as a game, news crawler, and portfolio.

**Agent error and correction:** The agent pushed toward free-form personalization while underexplaining its limits. It conflated text capture, interpretation, generated code, and generated teaching. When challenged, it then prematurely recommended live AI as required. James identified that this overlooked his template-based approach.

**Status:** Supported templates and authored teaching are the baseline. Catalog size, supported combinations, and live AI remain open.

**Process lesson:** Every capability proposal must identify what makes it possible, its limits, and whether it has been verified. Separate learner intent, execution, curriculum, and assessment.

## 007 — The intended workspace is concrete

**James's concept:** Select a template, then use a split screen with agent/tasks on the left and a working project preview on the right. He asked whether this could use a real local browser/development server similar to his Codex workflow.

**Status:** Split-screen interactive preview established; runtime choice open.

**Evidence:** Official WebContainers documentation describes Node.js execution and preview embedding in-browser. This does not establish that it meets every template, local-file requirement, or security constraint. A local companion is a separate candidate requiring a feasibility test.

## 008 — Build a mental model before asking learners to diagnose

**James's reasoning:** Software technology names currently feel like an undifferentiated block of text. By contrast, he can deconstruct a computer into hardware components and follow a troubleshooting sequence when it fails.

**Status:** Central learning-model clarification.

**Implication:** Connect the actual code to a visible system map. Teach component responsibilities and data flow before relying on bug-identification exercises. Proposed progression: locate, trace, explain, investigate, verify.

## 009 — Security oversight has a real personal consequence

**James's account:** An agent placed a private API credential in frontend code. He did not recognize the exposure, and unauthorized usage cost him over $100.

**Status:** User-reported experience, not independently audited. Do not disclose the credential, service account, or identifying incident details.

**Implication:** Teach browser/server trust boundaries through code and observable behavior, and apply those protections to the learning platform itself. Use fake secrets and mock services in exercises.

## 010 — Explain decisions, not just produce a functioning app

**James's reasoning:** He can use Codex to ship useful applications but would struggle to explain why code choices were made in an interview.

**Status:** Established success criterion.

**Implication:** Evaluate the ability to reconstruct behavior, compare alternatives, and support an explanation with evidence. Do not present an agent's plausible retrospective explanation as proof of the original intent.

## 011 — Understand why a stack fits a workload

**James's reasoning:** As with selecting hardware for a specific need, he wants to understand when Python, Rust, Go, C, TypeScript, or another technology is suitable and why.

**Example:** A social-media claim about a large memory reduction from TypeScript to Rust prompted a desire to understand the mechanism rather than memorize the outcome.

**Status:** Established curricular requirement; the specific post and claim were not verified.

**Implication:** Teach workload, representation, runtime, ecosystem, constraints, and maintenance through comparisons. Use equivalent measured examples and distinguish facts from unsupported numerical claims.

## 012 — Python and live AI are separate decisions

**James's proposal:** Python might fit deterministic prompt evaluation; he explicitly described this as a hypothesis rather than an expert conclusion.

**Clarification:** Python can implement explicit checks, but does not make arbitrary language interpretation deterministic. Assessing behavior, assessing intent, and generating lessons have different requirements.

**Status:** No language selected. James asked to evaluate the need for live AI later; subsequent discussion did not finalize adoption.

## 013 — Make the engineering process usable by smaller models

**James's constraint:** Planning uses GPT-6 Astra, while much implementation will use GPT-5.6 models down to Luna because of cost.

**Status:** Established delivery constraint.

**Agent proposal:** Small tasks with explicit contracts, fixtures, acceptance evidence, review gates, and empirical benchmark tasks. Escalate unresolved consequential decisions rather than asking a smaller model to invent architecture. No model-cost or capability claims have been measured in this project.

## 014 — Preserve reasoning as portfolio evidence

**James's request:** Keep a log of his reasoning for a later portfolio artifact. He explicitly wants to discuss AuDHD and spread awareness.

**Status:** Established documentation requirement and approved narrative direction.

**Implication:** Credit James's insights, identify agent suggestions and corrections, retain uncertainty, and link later decisions to PRs and test evidence. Public publication and repository visibility were unresolved at this point; entry 016 records the later decision.

## 015 — Consolidate now; ask remaining questions later

**James's instruction:** Finish a plan based on the conversation while he eats; he will ask for remaining questions when he returns.

**Status:** This planning draft and journal fulfill the consolidation request. No application implementation or paid provisioning is part of this step.

**Next:** Review the plan, then resolve its questions one at a time. Do not convert proposed defaults into approved decisions merely because James is away.

## 016 — Establish a public review history

Date: September 26, 2026.

**James's decision:** Publish the repository publicly and keep it suitable for hiring managers as development proceeds. He approved an initial main commit followed by a separate planning branch and pull request.

**Reasoning:** The existing goal is to make both the product and the engineering decisions available as portfolio evidence. A reviewed planning change establishes the workflow before application implementation.

**Outcome:** Created [the public repository](https://github.com/Angry-TacoZ/learning-to-code-with-audhd) with a minimal project overview on main. Planning documents are proposed in [draft PR #1](https://github.com/Angry-TacoZ/learning-to-code-with-audhd/pull/1) on codex/project-plan. The README clearly distinguishes intended capabilities from implemented behavior.

**Verification:** The documentation check passed locally and in GitHub Actions. Temporary fixtures confirmed that the checker rejects missing file links, conflict markers, trailing whitespace, and a tracked private configuration filename. Main requires a PR, the documentation check, and resolved conversations, with admin enforcement and force pushes disabled. No approving-review count is required for this solo repository; independent review remains a process requirement rather than an enforced approval. GitHub secret scanning, push protection, and private vulnerability reporting are enabled.

**Boundaries:** No application stack, hosting service, or license was selected. Public source does not imply public access to future learner data. The initial repository check validates documentation and file hygiene, not application security or teaching effectiveness.
