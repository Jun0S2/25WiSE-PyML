# PyML project (first part): setup

The PyML project overall consists of three stages:

1. Setup (environment, packaging, git, basic dir tree/architecture, etc.)
2. Infrastructure code (code **without** ML)
3. Experimenting with diffusion models using (1-2)

The first part focus on (1-2).

General remarks:

- If you know what you are doing, you can break "rules".
- We recommend viewing the task files in a Markdown preview editor (e.g., in VSCode)
- We encourage communicating with other students in the tutorials or the ISIS discussion forum, e.g., to ask questions, present your code and get feedback, or to learn about different perspectives.
- This project might include some (minor) tasks that were not (yet) covered in the lectures or tutorials. Feel free to ask AIs for help.

## Setup

Before starting the coding tasks, we encourage a helpful setup. The setup will mostly not be directly exam-relevant, e.g., we will not ask you to install a package manager during the exam. However, a good setup will help you to manage more complexity later, and it will also be beneficial for projects outside of the PyML course.

**Note that the task deliverable already provides some setup files.** Feel free to adjust those files as you prefer.

### Package/Environment manager

A package manager downloads and installs existing libraries such as NumPy and Torch, usually from the [PyPI index](https://pypi.org/). Note that you can also publish your own packages.
An environment manager ensures a project uses the exact package versions required by the project. This keeps things consistent because even minor version differences can cause code to behave unexpectedly.
Today, package managers and environment managers are often bundled into a single tool, such as Astral UV.

Please use [Astral UV](https://docs.astral.sh/uv/), **even if you already have another working solution**. Astral UV is **significantly** better than all alternatives we are aware of. Please also use a modern setup with files defining your environment, e.g., `pyproject.toml`, `.python-version`, and a `uv.lock`.

Note that modern package/environment managers might be more powerful than you think. We recommend reading the following blogpost: [uv is the best thing to happen to the Python ecosystem in a decade](https://emily.space/posts/251023-uv)

### Formatters/linters/... and pre-commit hooks

Many tools can review your code and point out style issues, common mistakes, or other problems that lower its quality. Furthermore, such tools can ensure that multiple collaborators write code in a consistent style without explicitly and repeatedly aligning on it.

We recommend using formatters/linters (like `ruff`), static type checkers (like `mypy`), and **optionally** additional libraries like `pytest`, `vulture` (e.g., to find dead code), or [`jaxtyping`](https://github.com/patrick-kidger/jaxtyping) (automatically check shape consistency of tensor code). You can conveniently run those libs with [pre-commit](https://pre-commit.com/), either manually (via `pre-commit run --all-files`) or automatically on each commit (by registering the hook). Note that type checkers might **sometimes** be net-negative for fast development. Hence, we recommend turning type checkers on or off depending on context.

Tips:

- You can pipe the output of the above tools to AI-agents (or let AI agents use those tools directly).
- You can require AI agents to execute tests (e.g., via `pytest`) before suggesting code. You can also use AI agents to help write tests themselves (but please still understand every line of code!).

Note: Python does not require types, but specifying types can not only improve readability, but also allow using static type checkers. "static" means that the type checks do **not** execute at runtime. Note that Python ignores specified types at runtime.

### git

A version control system, like Git, tracks changes in your code. For example, it lets you safely experiment by creating separate feature branches for different versions of your project, or by returning to earlier commits to fix mistakes or bugs. It can also help with collaboration. For the PyML project, we encourage you to first work individually, then discuss or collaborate with others.

You can create a repository on GitHub or (TUB) GitLab. Learn [when to commit](https://medium.com/%40asifnahian/git-how-often-should-you-commit-c133e5473d76) changes. Include [meaningful messages](https://cbea.ms/git-commit/) with every commit. Learn how to use feature branches, squash/merge MRs or PRs, and the difference between linear and non-linear commit histories. Use a `.gitignore` file.

Ressources:

- [./missing-semester/Version Control (Git)](https://missing.csail.mit.edu/2020/version-control/)
- [An open source game about learning Git](https://ohmygit.org/)
- [Tips from the JuML course at TUB](https://adrianhill.de/julia-ml-course/git/)

### IDE

An IDE (Integrated Development Environment) is a program for writing code and developing software projects.
We recommend VSCode (free in general) or PyCharm ([free](https://education.github.com/pack) as a student). PyCharm natively offers many features, whereas VSCode can only achieve similar capabilities by installing various extensions. We recommend reviewing online resources to find popular extensions. You may also consider a VSCode fork like Cursor or Windsurf for additional AI capabilities (but please use them deliberately and cautiously within this project).

### AI

**Minimize the use of AI to *write* code:**

- Manually writing code gives you direct feedback on your weaknesses. Your weaknesses can regard the code directly (e.g., syntax) and your mental models, which you use to understand problems and generate solution candidates. Reducing your weaknesses via manual coding will make you more flexible in the exam, which requires skill transfer to variations of problems covered in the course. AI will **not** be available during the exam.
- If you use AI for code generation (e.g., to generate tests or to be able to scale this project to above-average complexity), be sure to understand **all** of the code produced **in detail**. As another idea, you may first solve a task yourself, then ask AIs to generate alternate solutions for your review.
- Note: Beyond PyML, we usually **encourage** the (deliberate) use of AI for your programming, e.g., for a degree thesis. However, PyML primarily tests your basic programming skills & not your use of AI. Improving basic skills should transfer well to coding with AI-assistance in other contexts.

**AI is helpful outside of code generation.** For example, it can be used to review or validate code, brainstorm solution candidates, provide tutoring and explanations, or generate practice tasks.

As a student, you have free access to [GitHub Copilot](https://education.github.com/pack) (this comes with GitHub Pro). Likewise, students can get a free year of [Gemini](https://gemini.google/sg/students/?hl=en) (until Dec 9th), which includes [Gemini Code Assist](https://codeassist.google/). Further, if you have a ChatGPT or Claude subscription, these include access to [Codex](https://openai.com/codex/) or [Claude Code](https://www.claude.com/product/claude-code), respectively.

## Coding: best practices

### Code of low (cognitive) complexity

You should usually aim for code of [minimal (cognitive) complexity](https://minds.md/zakirullin/cognitive). **This project is different**, because PyML is subject to time and exam-format constraints, i.e., PyML can only offer relatively simple tasks. However, the course's goal is to also teach patterns for larger projects. Hence, we encourage experimentation with varying levels of code complexity **while clearly understanding the trade-offs and how different levels of complexity would be helpful or harmful in practice.** For example, you could try writing a custom dataloader, even though Torch already offers one out of the box. Or you could write custom decorators and dunder methods to understand those concepts better.

### Frequent refactoring

Perhaps you learn the most by frequently challenging your previous ideas and mental abstractions. **This means to rewrite your code often and "throw away" a lot of previous work.** If you do **not** rewrite and throw away, you likely don't learn aggressively enough.

Furthermore, this project will accompany you until the exam period. Hence, you will learn **new** concepts in future lectures and tutorials. We encourage you to periodically evaluate how those new concepts relate to your existing code: Could they help add new features, reduce complexity, or improve readability? If they are not immediately helpful: what would be the settings in which the newly learned pattern would prove helpful?

### Further tips

- Aim for independent abstractions, e.g., avoid [spaghetti](https://en.wikipedia.org/wiki/Spaghetti_code) and ravioli code.
- Classes should have states. Otherwise, use functions.
- Variable names should be semantically meaningful.
- Avoid deep inheritance (adds complexity).
- Use the [rule of three](https://en.wikipedia.org/wiki/Rule_of_three_(computer_programming)) for refactoring (avoid refactoring too early or too late).
- Comments should primarily focus on non-obvious intent, not on the "code mechanics". Assume they are written for an expert Python programmer. Do not add too many comments.
- Do not write code "too defensively", e.g., avoid frequent try/except patterns as often suggested by AIs. Your code should be targeted at ML developers; the PyML project does not build an API for the general public (which would imply different requirements).
