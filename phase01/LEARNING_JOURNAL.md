# Phase 01 — Learning Journal

## Phase 01: Math Foundations

This journal records my practical learning as I study the mathematical foundations of AI engineering.

My goal is not just to complete lessons. I want to understand the mathematics, explain it in my own words, implement it in Python, and gradually solve problems with less guidance.

---

## Lesson 01 — Vectors

**Date:** 2026-11-19

**Status:** Completed

### What I Worked On

I studied vectors and implemented six vector operations in Python in:

`01-linear-algebra-intuition/vectors.py`

The operations I implemented were:

1. Vector magnitude
2. Vector addition
3. Vector subtraction
4. Scalar multiplication
5. Dot product
6. Vector normalization

I also organized the program using functions and a `main()` function.

### What I Understood

- A vector represents quantities with magnitude and direction.
- Vector magnitude tells me the length of a vector.
- Vector addition combines corresponding components.
- Vector subtraction subtracts corresponding components.
- Scalar multiplication multiplies every component by a number.
- The dot product combines corresponding components through multiplication and addition.
- Normalization changes a non-zero vector to have a magnitude of 1 while preserving its direction.

### What I Practised in Python

I practised:

- Writing functions with parameters.
- Returning calculated results.
- Working with lists and list indexes.
- Using `math.sqrt()` to calculate square roots.
- Using `if` statements to check for a zero vector.
- Raising a `ValueError` when normalization is not possible.
- Handling errors with `try` and `except`.
- Organizing code with `main()` and `if __name__ == "__main__":`.

### Challenges

I initially used `VectorError` instead of the correct built-in exception, `ValueError`.

This caused a `NameError` because Python did not recognize `VectorError` as a defined name.

### How I Fixed It

I corrected the exception to:

`raise ValueError("Cannot normalize a zero vector")`

I then tested the zero-vector case using `try` and `except`.

### What I Tested

I tested vector magnitude with:

- `[3, 4]` → `5.0`
- `[6, 8]` → `10.0`
- `[5, 12]` → `13.0`

I also tested vector addition, subtraction, scalar multiplication, dot product, and normalization.

For normalization:

- `[6, 8]` → `[0.6, 0.8]`
- `[3, 4]` → `[0.6, 0.8]`

For the zero vector `[0, 0]`, my program raised and handled the expected `ValueError`.

These were manual program checks, not a separate automated test suite.

### What I Learned

I learned that implementing a mathematical formula in Python requires more than knowing the formula.

I also need to:

- Break the problem into smaller steps.
- Choose the right variables and operations.
- Write functions that perform clear tasks.
- Think about special cases.
- Read errors and correct mistakes.
- Test different inputs.

### What I Did Well

I completed all six vector operations, corrected my exception error, tested different inputs, and committed and pushed my work to GitHub.

### What I Need to Improve

I still need more practice with:

- Explaining mathematical ideas without looking at notes.
- Writing Python functions independently.
- Understanding mathematical formulas before coding them.
- Designing automated tests.
- Finding and correcting errors with less guidance.

### Git Record

**Commit:** `3761c3b`

**Commit message:** `feat: add vector normalization and error handling`

The code was pushed to GitHub, and the working tree was clean after the push.

### Next Action

Continue with the next Phase 01 lesson.

I will keep using the same learning process:

1. Understand the concept.
2. Explain it in my own words.
3. Work through pseudocode.
4. Implement it in Python.
5. Test my implementation.
6. Record what I learned and what I need to improve.