# Lesson 3.4: `Django` Project Creation 🌐

## Description 📝

This lesson guides the creation of a **`Django` project** for **`Yatube`**, a social network for personal diaries. It covers setting up a `Git` repository, virtual environment, `Django` installation, project and application creation, and preparing for the first commit.
This lesson includes a theoretical overview, 6 practical tasks, and 1 reflection task, focusing on initializing a `Django` project.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Set up a `Git` repository and virtual environment for a `Django` project  
✅ Install and configure `Django 2.2.19` for `Yatube`  
✅ Create and launch a `Django` project with a development server  
✅ Initialize a `Django` application and prepare project files for version control

## Concepts & Theory 🔍

### 🔹 `Yatube` Project

-   **Purpose**: Social network for blogging with user accounts, posts, comments, subscriptions, and moderation.
-   **Design**: Minimalistic, text-focused interface.
-   **Documentation**: Includes concept, technical requirements, user stories, and mockups (only concept used for `Yatube`).

### 🔹 `Django` Setup

-   **Environment**: `GitHub` repository (`yatube_project`), virtual environment, Visual Studio Code (`VSC`) integration.
-   **`Django` Installation**: Version 2.2.19 (LTS) with dependencies (`pytz`, `sqlparse`).
-   **Project Structure**: Includes `manage.py`, `settings.py`, `urls.py`, `wsgi.py`.
-   **Applications**: Modular components (e.g., `posts`) registered in `settings.py`.

### 🔹 Version Control

-   **Git**: Repository creation, `.gitignore` setup, first commit.
-   **Files**: `README.md` (project overview), `requirements.txt` (dependencies), `LICENSE` (e.g., `MIT`).

## Practical Task 🧪

### 1️⃣ **`Django` Project Initialization**

The lesson includes 6 practical tasks and 1 reflection task:

1. **Create Repository (yatube_project)**: Set up a private GitHub repository with `README.md`, `.gitignore` (`Python` template), and license (`MIT`/`BSD 3`). Clone to local machine.
2. **Install `Django`**: Activate virtual environment, install `Django 2.2.19`, configure `VSC` to use virtual environment Python.
3. **Create Project**: Run `django-admin startproject yatube` and verify project structure.
4. **Launch Server**: Start development server with `python manage.py runserver` and check `http://127.0.0.1:8000/`.
5. **Prepare Commit**: Update `.gitignore` (add `.vscode/`, `venv/`), generate `requirements.txt`, format `README.md`, and push initial commit.
6. **Create Application**: Create `posts` application with `python manage.py startapp posts` and register in `settings.py` as `posts.apps.PostsConfig`.
7. **Reflection**: Document challenges, Markdown editor used, benefits of `PostsConfig`, and errors encountered in a diary.

💡 Tasks establish a solid foundation for `Django` development and version control.

## Benefits ✅

-   Structured setup ensures a scalable `Django` project.
-   Virtual environments isolate dependencies for consistency.
-   `Git` integration supports collaborative development.
-   Early server testing confirms project functionality.

## Recommendations 📌

-   Verify `.gitignore` includes `.vscode/` and `venv/` to avoid committing unnecessary files.
-   Use `pip freeze > requirements.txt` to track dependencies accurately.
-   Test the development server (`http://127.0.0.1:8000/`) before committing.
-   Keep `README.md` clear and professional for project documentation.

## Output 📜

After completing this lesson, I now:  
✅ Create and configure a `Git` repository for a `Django` project  
✅ Install and set up `Django 2.2.19` with a virtual environment  
✅ Initialize a `Django` project and application  
✅ Prepare and commit project files with proper documentation

## Conclusion 🚀

Setting up the `Yatube Django` project marks a key step in mastering web development.  
By establishing a robust project structure and environment, I’m ready to build a functional social network, leveraging `Django’s` power for rapid, professional-grade development. 🧑‍💻✨
