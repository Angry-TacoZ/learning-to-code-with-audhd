# Contribution workflow

The application is being planned. Architecture and curriculum proposals are welcome as focused issues or pull requests; unresolved choices in the [plan](docs/implementation-plan.md) should be settled before dependent implementation.

## Proposing a change

1. Describe the learner problem, expected result, and scope. For substantial implementation, open an issue with acceptance criteria before coding.
2. Work on a focused branch, using codex/<short-purpose> for agent-assisted work.
3. Inspect related behavior and record meaningful decisions in the [journal](docs/decision-journal.md).
4. Stage intended files and run `python scripts/check_docs.py` and `git diff --cached --check`.
5. Open a PR targeting main with the rationale, verification evidence, and remaining limits. Identify agent assistance and the human review still needed.

The current check validates tracked Markdown links to local files, whitespace, conflict markers, and a small set of filenames that should not be committed. It does not check external links or serve as a secret scanner. Python 3 is sufficient; no packages need installing.

## Review and merge

Keep planning PRs in draft while product decisions are being discussed. Passing CI verifies the stated checks, not the entire proposal. James makes the merge decision. An author cannot supply an independent approving review of their own PR; record review limitations honestly.

Main is protected: a pull request, the Documentation checks status, and resolved review conversations are required, including for administrators. Force pushes and branch deletion are disabled. The approving-review count is zero for this solo repository; independent review is a process expectation, not an enforced second-person approval.

Once code exists, require tests for the changed behavior, negative security cases where relevant, and inspection of the running output for UI changes. Add those checks to CI as part of implementation.

## Public information

Use synthetic examples. Do not attach credentials, private user content, or unreviewed conversation exports. Follow [the security policy](SECURITY.md) for vulnerabilities. Repository licensing is pending; do not assume public visibility grants permission to reuse its contents.
