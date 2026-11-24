# Phase 01 — Learning Journal

## Phase 01: Math Foundations

This journal records my practical learning as I study the mathematical foundations of AI engineering.

My goal is not just to complete lessons. I want to understand the mathematics, explain it in my own words, implement it in Python, and gradually solve problems with less guidance.

---

# Lesson 01 — Vectors

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

---

# Lesson 02 — Vectors, Matrices & Operations

**Date:** 2026-11-24

**Status:** In Progress

### What I Worked On

I started learning about matrices and how to calculate their shape using Python.

My exercise is in:

`02-vectors-matrices-operations/matrix_shape.py`

### What I Understood

- A matrix is a rectangular arrangement of numbers organized into rows and columns.
- Rows run horizontally.
- Columns run vertically.
- Matrix shape is written as rows × columns.
- `len(matrix)` counts the rows.
- `len(matrix[0])` counts the columns in the first row.
- Total elements = rows × columns.
- Python lists use zero-based indexing, so `matrix[0]` accesses the first row.

### What I Practised in Python

I practised:

- Creating nested lists.
- Storing values in variables.
- Using `len()` to count rows and columns.
- Accessing a list inside another list.
- Multiplying values.
- Displaying results with `print()`.

### The Five Learning Stages

I completed the five stages for my first matrix-shape exercise:

1. **Understand the concept before writing code:** I learned what matrices, rows, columns, and dimensions mean.
2. **Break the problem into smaller pieces:** I identified how to create the matrix, count rows, count columns, calculate total elements, and display results.
3. **Work through pseudocode:** I planned the steps before implementation.
4. **Attempt the implementation myself:** I wrote and improved the Python program.
5. **Test my understanding and implementation:** I tested different matrices and explained their dimensions.

### What I Tested

| Matrix shape | Expected total | Result |
|---|---:|---|
| 3 × 2 | 6 | Passed |
| 2 × 4 | 8 | Passed |
| 4 × 3 | 12 | Passed |

These were manual program checks, not an automated test suite.

### Challenge and How I Fixed It

I initially used fixed row and column values.

I learned that hardcoded values do not automatically change when the matrix changes.

I corrected this by calculating the dimensions directly from the matrix:

- `row = len(matrix)`
- `column = len(matrix[0])`

This made the program dynamic.

### What I Learned

I learned that a good program should calculate values from its actual input instead of relying on numbers that I manually enter into the code.

I also learned why breaking a problem into smaller steps makes implementation easier.

### What I Did Well

I completed my first matrix-shape exercise, tested three different matrix sizes, corrected my hardcoded dimensions, and pushed the updated code to GitHub.

### What I Need to Improve

I need more practice with:

- Creating nested lists independently.
- Explaining matrix dimensions without looking at notes.
- Understanding matrix operations.
- Writing automated tests.
- Solving exercises with less guidance.

### Git Record

**Commit:** `e4ff469`

**Commit message:** `feat: calculate matrix dimensions dynamically`

The updated code was successfully pushed to GitHub.

### Next Action

Continue Phase 01, Lesson 02 by learning the next matrix operation.

I will continue using the five-stage learning process and practise implementing solutions myself before receiving complete answers.