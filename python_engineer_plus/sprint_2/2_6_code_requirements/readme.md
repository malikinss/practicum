# Lesson 2.6: Code Requirements 📜

## Description 📝

This lesson covers **code style requirements** in `Python`, focusing on **`PEP 8`** guidelines, **`docstrings`** (`PEP 257`), and the use of **linters** like `flake8` to ensure consistent, professional code.

This lesson includes a detailed theoretical explanation, **no practical programming tasks**, and **no theoretical questions**, emphasizing code formatting and documentation standards.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Understand and apply `PEP 8` for consistent code formatting  
✅ Write clear, professional docstrings per `PEP 257 `
✅ Use `flake8` to automate code style checks  
✅ Ensure my code meets professional and project standards

## Concepts & Theory 🔍

### 🔹 `PEP 8`

-   **Purpose**: Standard for `Python` code style to enhance readability and consistency.
-   **Key Rules**:
    -   Max `79` characters per line.
    -   `4-space` indents (no tabs).
    -   Naming: `snake_case` for variables/functions, `CamelCase` for classes.
    -   Imports: Ordered (standard library, third-party, local), remove unused.
    -   Blank lines: `2` between functions/classes, `1` between class methods.
    -   Quotes: Prefer single quotes (`'`) with nested double quotes (`"`).

### 🔹 `Docstrings` (`PEP 257`)

-   **Purpose**: Document modules, functions, and classes for clarity.
-   **Format**: Triple quotes (`"""`), capitalize first letter, end with a period.
-   **Placement**: Immediately after definition.
-   **Access**: Via `__doc__` attribute or `inspect.cleandoc`.
-   **Styles**: Google, numpydoc, or simple descriptions.

### 🔹 Linters

-   **Purpose**: Static analysis tools to enforce style and catch errors.
-   **Primary Tool**: `flake8` (combines `pycodestyle`, `pyflakes`, `mccabe`).
-   **Add-ons**: `pep8-naming`, `flake8-broken-line`, `flake8-return`, `flake8-isort`.
-   **Setup**: Install via `pip install flake8`, integrate with VS Code.

## Practical Task 🧪

### 1️⃣ **No Practical Tasks**

This lesson focuses on theoretical understanding of `PEP 8`, docstrings, and linters, with practical application through setting up `flake8` and writing compliant code. No standalone coding tasks are assigned.

## Benefits ✅

-   `PEP 8` ensures readable, maintainable code.
-   Docstrings document functionality for collaboration.
-   Linters automate style checks, reducing manual errors.
-   Professional formatting enhances project credibility.

## Recommendations 📌

-   Run `flake8` regularly to catch style issues early.
-   Write concise, meaningful docstrings for all public functions/classes.
-   Configure `VS Code` with `flake8` for real-time feedback.
-   Follow `PEP 8` strictly for Yandex Practicum project acceptance.

## Output 📜

After completing this lesson, I now:  
✅ Apply `PEP 8` guidelines for consistent code style  
✅ Write professional docstrings per `PEP 257`  
✅ Use `flake8` to enforce coding standards  
✅ Produce clean, maintainable code for team projects

## Conclusion 🚀

Mastering `PEP 8`, docstrings, and linters elevates my `Python` code to professional standards.  
By adhering to these guidelines, I ensure my projects are readable, maintainable, and ready for collaboration in real-world development. 🧑‍💻✨
