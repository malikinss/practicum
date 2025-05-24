# Lesson 2.4: Environment 🛠️

## Description 📝

This lesson covers setting up a development environment, including **Git** for version control, **GitHub** for collaboration, **virtual environments** (`venv`) for project isolation, and **pytest** for automated testing.

This lesson includes a detailed theoretical explanation, **no explicit practical programming tasks**, and **no theoretical questions**, focusing on environment setup and tool usage.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Configure Git and GitHub for version control  
✅ Clone repositories and manage file states with Git commands  
✅ Set up and use virtual environments for project isolation  
✅ Run automated tests with pytest and troubleshoot issues

## Concepts & Theory 🔍

### 🔹 Git

-   **Purpose**: Version control system for collaborative development.
-   **Features**: Tracks changes, resolves conflicts, manages project versions.
-   **Popularity**: Used by ~70% of developers.

### 🔹 GitHub

-   **Purpose**: Platform for hosting Git repositories and collaboration.
-   **Features**: Stores code, supports forking, and hosts GitHub Pages.
-   **Setup**: Requires account creation and email verification.

### 🔹 Git Workflow

-   **Repository**: Stores project files and history.
-   **Commands**:
    -   `git clone`: Copies a remote repository locally.
    -   `git status`: Shows file states (untracked, staged, modified, committed).
    -   `git add`: Stages changes for commit.
    -   `git commit`: Saves changes with a message.
    -   `git push`: Uploads commits to GitHub.
    -   `git log/show/reset`: Manages commit history.
-   **`.gitignore`**: Excludes specified files from tracking.

### 🔹 Virtual Environment (`venv`)

-   **Purpose**: Isolates project dependencies to avoid conflicts.
-   **Commands**:
    -   `python3 -m venv venv`: Creates environment.
    -   `source venv/[Scripts|bin]/activate`: Activates environment.
    -   `deactivate`: Exits environment.

### 🔹 Pytest

-   **Purpose**: Runs automated tests for Python code.
-   **Setup**: Install via `pip install pytest` in active `venv`.
-   **Usage**: Run `pytest` to test files like `test_program.py`.

### 🔹 Windows Encoding Fix

-   **Issue**: Cyrillic text in `pytest` output may be unreadable in Git Bash.
-   **Solution**: Set `ru_RU.UTF-8` and `UTF-8` in Git Bash settings or use VS Code terminal.

## Practical Task 🧪

### 1️⃣ **No Explicit Practical Tasks**

This lesson focuses on hands-on setup of Git, GitHub, `venv`, and `pytest`, with practical application through repository cloning, environment creation, and test execution. No standalone coding tasks are assigned.

## Benefits ✅

-   Git enables collaborative, versioned development.
-   Virtual environments ensure project-specific dependency management.
-   Pytest automates testing for reliable code.
-   Environment setup skills are foundational for professional workflows.

## Recommendations 📌

-   Configure `user.name` and `user.email` for Git commits.
-   Use `.gitignore` to exclude unnecessary files.
-   Always activate `venv` before installing packages or running tests.
-   Check `pytest` output to debug and fix code errors.

## Output 📜

After completing this lesson, I now:  
✅ Set up Git and GitHub for version control  
✅ Clone and manage repositories with Git commands  
✅ Create and use virtual environments for isolation  
✅ Run and troubleshoot tests with pytest

## Conclusion 🚀

Mastering Git, virtual environments, and pytest establishes a robust development environment.  
By configuring these tools, I’m equipped to collaborate, test, and manage Python projects like a professional developer. 🧑‍💻✨
