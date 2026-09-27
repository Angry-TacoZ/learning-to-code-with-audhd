# Project guidance

## Purpose

Help James build a learning application for understanding and reviewing agent-written software. Read README.md, docs/implementation-plan.md, and the relevant decision-journal entries before proposing changes. This project is in planning; do not choose a stack or implement unresolved architecture implicitly.

## Working with James

- Ask about consequential unknowns one at a time. Explain at least two project-specific options when choosing technologies.
- Keep explanations plain and connect technology names to their role in the system.
- For substantial engineering changes, offer a walkthrough after completion.
- End responses with the technologies actually used that turn.

## Changes and evidence

- Inspect the repository and directly related files before editing. Keep tasks bounded and provide observable acceptance criteria.
- Use codex/<short-purpose> branches and PRs targeting main. Do not merge unless James requests it.
- State what was verified and what remains open. Do not present planned features, tests, or deployments as existing capabilities.
- Run `python scripts/check_docs.py` after staging intended files and `git diff --cached --check` before committing. The script inspects tracked files, including staged additions.
- No application build or runtime test command exists yet. Add appropriate verification when the implementation begins.
- Smaller-model tasks need explicit inputs, expected outputs, edit boundaries, examples, and verification commands. Escalate unresolved architecture or security questions instead of guessing.

## Public portfolio record

- Keep the README concise and accurate for a hiring manager encountering the project for the first time.
- Record meaningful decisions in docs/decision-journal.md. Distinguish James's reasoning, agent proposals, and verified evidence. Preserve earlier uncertainty and corrections.
- James has chosen to discuss AuDHD openly. Do not publish medication details, private conversation transcripts, credentials, personal filesystem paths, or learner data.
- Keep new public claims linked to evidence where possible. Public visibility is approved; application release and paid provisioning are separate actions.

## Security

- Never commit private credentials or place them in browser code. Use synthetic fixtures for lessons.
- Treat learner/project code as untrusted; it must not receive platform credentials or run in the platform API process.
- Do not weaken checks, authorization, or runtime boundaries to make an example pass.
- Review SECURITY.md before reporting a vulnerability publicly.
