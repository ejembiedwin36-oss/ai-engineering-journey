# AI Engineering Learning Journal

This journal records my personal growth throughout my AI Engineering journey.

It is not only a record of what I completed. It also captures the problems I faced, mistakes I made, how I solved them, what I learned from them, and the strengths I am developing.

---

## How I Will Use This Journal

For each important lesson, project, challenge, or breakthrough, I will record:

- What I worked on
- What I understood
- What challenged me
- What failed
- Why it failed
- How I fixed it
- What I learned from the experience
- My strengths
- What I still need to improve
- My next action

---

# Phase 00 — Setup and Tooling

**Status:** ✅ Completed

## What I Achieved

During Phase 00, I learned and practiced:

- Setting up a development environment
- Python and virtual environments
- Git and GitHub
- GPU and cloud basics
- APIs and environment variables
- Jupyter Notebooks
- Docker and Docker Compose
- VS Code setup
- Data management
- Terminal and shell commands
- Linux fundamentals
- Debugging and profiling
- Core Python for AI Engineering
- Generators and mini-batching
- CSV and JSON processing
- Train/test splitting
- Vector mathematics
- Standardization
- Basic classification
- Measuring speed and memory
- NumPy broadcasting

---

## Challenges and Failures

### 1. Working on a Resetting School Computer

**Challenge:**  
The school/lab computer could lose installed software and unpushed work after logout or reset.

**What I learned:**  
Local files should never be treated as the only copy of important work.

**How I handled it:**  
I started committing and pushing important checkpoints regularly to GitHub.

**Lesson:**  
GitHub is not only for showing code. It is also a safety system for my work.

---

### 2. Python Environment and Dependency Problems

**Challenge:**  
Some packages and commands were unavailable after moving between computers.

**Examples:**
- Python environments disappearing
- NumPy not being installed
- Dependency installation problems
- Large environment installations taking too long

**How I handled it:**  
I learned to:
- Create a virtual environment
- Activate `.venv`
- Install only the package I needed when appropriate
- Check installed versions
- Avoid reinstalling unnecessary large dependencies

**Lesson:**  
A good AI engineer understands the environment the code runs in, not only the code itself.

---

### 3. Git and GitHub

**Challenge:**  
I had to understand commits, pushes, pulls, branches, remotes, and how to protect my work.

**How I improved:**  
I repeatedly used:

```bash
git status
git add
git commit
git push
git pull
git log
```

I also learned how Git recognizes file moves and how to reorganize a repository without losing history.

**Lesson:**  
I am becoming more confident using Git as part of my normal development workflow.

---

### 4. Understanding Generators

**Challenge:**  
Generators were initially confusing because they do not behave exactly like lists.

**Important discovery:**  
A generator is consumed after it has been used.

This matters in AI because training code may need to iterate through data again for another epoch.

**Lesson:**  
I now understand why data pipelines must often create a fresh generator for each epoch.

---

### 5. Python Performance

**Challenge:**  
I needed to understand why different Python approaches performing the same calculation have different speeds.

**My experiment showed approximately:**

- Index loop: slower
- Generator expression: similar/slower
- `map()` with `operator.mul`: faster

I also compared memory usage:

- List: about 4 MB peak
- Generator: only a few hundred bytes peak

**Lesson:**  
Readable code, execution speed, and memory usage can all matter in AI engineering.

---

### 6. NumPy and Broadcasting

**Challenge:**  
I first built standardization manually in pure Python.

Later I used NumPy broadcasting to perform the same calculation.

**What I learned:**  
Instead of manually looping through every number, NumPy can operate over entire arrays efficiently.

This helped me understand why AI and machine-learning libraries rely heavily on arrays and tensors.

---

# My Strengths

## 1. Persistence

I do not easily stop when something fails.

Even when environments reset, installations fail, commands give errors, or code does not behave as expected, I keep working through the problem.

## 2. Asking Until I Understand

I do not want to only copy code.

I frequently ask what a line means, why something works, and why an error occurred.

This is helping me move from simply following instructions toward understanding the engineering behind them.

## 3. Learning Through Practice

I learn better when I type commands, run code, see the result, make mistakes, and fix them.

## 4. Willingness to Start Again

Changing computers and losing local setup has forced me to rebuild environments several times.

Although frustrating, this has strengthened my understanding of setup, Git, Python environments, and dependency management.

## 5. Gradual Improvement

Concepts that initially looked difficult are becoming more familiar through repetition.

---

# Areas I Need to Improve

- Writing Python without depending heavily on examples
- Reading errors independently before asking for help
- Understanding mathematical notation
- Becoming faster with Linux commands
- Writing tests
- Choosing good function and variable names
- Breaking large problems into smaller steps
- Explaining my own code clearly
- Understanding AI mathematics deeply

---

# Reflection Template

I will copy this section whenever I want to record a new important learning experience.

## Date

YYYY-MM-DD

## Phase / Lesson

Example: Phase 01 — Lesson 01

## What I Worked On

Describe what I studied or built.

## What I Understood

Explain the main ideas in my own words.

## Challenge

What was difficult?

## Failure / Error

What went wrong?

## Why It Failed

What caused the problem?

## How I Fixed It

Explain the steps I took.

## What I Learned

What will I remember from this experience?

## My Strength

What did I do well?

## What I Need to Improve

What should I practice more?

## Next Action

What will I do next?

---

# Personal Goal

My goal is not simply to finish lessons.

My goal is to become an AI engineer who can:

- Understand problems
- Write code independently
- Debug failures
- Explain technical decisions
- Learn from mistakes
- Build real systems
- Continue improving without depending completely on someone else

Every error I solve is part of the training.