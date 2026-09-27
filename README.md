# Learning to Code with AuDHD

A learning application in planning, focused on understanding, reviewing, and troubleshooting code written by AI agents.

Created by James Lane. My experience with autism and ADHD shapes the project: learning needs a visible payoff, room for personal interests, and a clear path back after a break.

The goal is to help learners build a mental model of software: what each component does, how components connect, where failures can occur, and why a particular technology fits a problem. The intended outcome is being able to explain and verify an agent's work.

## Proposed experience

- Choose a supported web project, such as a portfolio or browser game, and features that matter to you.
- Work through authored lessons beside a running project preview.
- Connect behavior on screen to small code changes and a map of the system.
- Practice tracing failures, checking security boundaries, and comparing technology choices.
- Resume from a clear next step, with optional depth and no fixed session length.

These are design requirements. Their usability and teaching effectiveness still need to be tested.

## Current stage

This repository is at the planning stage. There is no runnable application, deployed demo, or selected production stack yet. The first milestone is a small working learning experience that can test the proposed approach.

Live AI, the project runtime, and the launch template count remain open decisions. Prepared teaching content and agent execution are being evaluated separately.

## Design and engineering record

| Document | What it records |
| --- | --- |
| [Implementation plan](docs/implementation-plan.md) | Learning requirements, architecture options, security boundaries, and delivery gates |
| [Decision journal](docs/decision-journal.md) | My reasoning, agent recommendations, corrections, and unresolved questions |
| [Contribution workflow](CONTRIBUTING.md) | How changes are scoped, checked, and reviewed |

I use coding agents as implementation partners. This repository will record the requirements, decisions, reviews, and verification behind their output. Proposed architecture will remain labeled as proposed until a decision is made; a working demo will only be linked after it exists and has been checked.

Current CI checks the repository's documentation and file hygiene. Application tests, security evaluations, and deployment checks will be added with implementation; they are described in the plan and are not running yet.

To run the current check with Python 3:

```sh
python scripts/check_docs.py
```

Python is used here only for a dependency-free repository check. It does not select the application's backend language.

Follow the [pull requests](https://github.com/Angry-TacoZ/learning-to-code-with-audhd/pulls) for reviewed changes.

The working title is provisional. Licensing has not yet been selected.
