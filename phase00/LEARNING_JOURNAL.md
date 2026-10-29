# Phase 00 — Learning Journal

> **Purpose of this file**
>
> This file is my personal reflection journal for Phase 00 of my AI Engineering journey.
>
> It is different from the other documentation in this repository:
>
> - `README.md` explains the Phase 00 lessons in simple language so another beginner can learn from them.
> - `LEARNING_JOURNAL.md` records my personal experience: my challenges, mistakes, failures, fixes, strengths, lessons learned, and areas I need to improve.
> - The root `LEARNING.md` tracks my overall course progress and completed lessons.
>
> In simple terms:
>
> **README = What I learned and how to understand it**
>
> **LEARNING_JOURNAL = How I personally learned it**
>
> **LEARNING.md = My overall progress record**
>
> This journal is not meant to be a perfect technical guide. It is an honest record of my growth, including the things that went wrong and what I learned from fixing them.

---

**Phase:** Setup and Tooling  
**Status:** ✅ Completed

This journal records my personal experience during Phase 00: my challenges, failures, fixes, strengths, and areas I still need to improve.

---

## My Biggest Challenges

### Working on Different Computers

One major challenge was working on school/lab computers where my local setup could disappear after a reset or logout.

This taught me that important work should not exist only on one computer.

### How I solved it

I started committing and pushing important progress to GitHub regularly.

### What I learned

GitHub is not only a place to display projects. It can also protect my learning work.

---

## Environment Problems

Sometimes packages or tools that worked previously were unavailable on a new computer.

For example, NumPy was missing when I needed it during Lesson 13.

### How I solved it

I created a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Then installed only what I needed.

### What I learned

The code may be correct while the environment is the real problem.

---

## Git and GitHub

At the beginning, Git commands were unfamiliar.

Through repeated practice, I became more comfortable using:

```bash
git status
git add
git commit
git push
git pull
```

I also learned how to move files with `git mv` while keeping their Git history.

---

## Understanding Generators

Generators were initially confusing.

I learned that a generator produces values one at a time instead of storing everything in memory.

I also learned that a generator is consumed after it has been used.

This matters in AI training because the program may need fresh data for every training epoch.

---

## Performance and Memory

During Lesson 13, I measured different ways of calculating a dot product.

My machine showed approximately:

- Index loop: 9.69 ms
- Generator version: 10.14 ms
- `map()` version: 6.41 ms

I also compared memory usage:

- List peak: about 4,000,456 bytes
- Generator peak: about 464 bytes

### What I learned

Two programs can produce the same answer but use very different amounts of time and memory.

---

## NumPy Broadcasting

I first wrote feature standardization in pure Python.

Then I performed the same operation using NumPy broadcasting.

Both produced approximately:

```text
[[-1.225 -1.225]
 [ 0.     0.   ]
 [ 1.225  1.225]]
```

### What I learned

Understanding the pure-Python version helped me understand what NumPy was doing.

---

# My Strengths

## Persistence

When something does not work, I keep trying until I understand the problem.

## Asking Questions

I prefer to understand why something works instead of only copying code.

## Learning by Doing

I understand concepts better when I type the commands, run the code, make mistakes, and fix them.

## Starting Again

Working on different computers forced me to rebuild environments several times.

Although this was frustrating, it improved my understanding of setup and environments.

---

# Areas I Need to Improve

I still need to improve in:

- Writing Python independently
- Reading error messages before asking for help
- Remembering terminal commands
- Understanding mathematics
- Writing tests
- Explaining code without looking at notes
- Breaking problems into smaller steps

---

# Most Important Lesson From Phase 00

AI Engineering is not only about models.

An AI engineer also needs to understand:

- The development environment
- Source control
- Data
- Linux
- Debugging
- Performance
- Dependencies
- Reproducibility

Phase 00 gave me the foundation for these skills.

---

# Going Into Phase 01

My next focus is:

**Phase 01 — Math Foundations**

My goal is not to memorize formulas.

I want to understand:

1. What the mathematics means
2. Why AI uses it
3. How to calculate it
4. How to represent it in Python
5. How it connects to real AI systems

---

# Reflection Template for Future Entries

I can reuse this section whenever I want to record an important learning experience.

## Date

YYYY-MM-DD

## Lesson / Topic

What was I studying?

## Challenge

What was difficult or confusing?

## What Went Wrong

What failed or did not work as expected?

## Why It Happened

What caused the problem?

## How I Fixed It

What steps did I take to solve it?

## What I Learned

What do I understand now that I did not understand before?

## My Strength

What did I do well during this challenge?

## What I Need to Improve

What should I practice more?

## Next Action

What should I do next?