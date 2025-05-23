# OOP Interaction Simulation for Student, Mentor, CodeReviewer, and Curator

## Description 📝

The provided code implements a system to model interactions between a `Student`, `Mentor`, `CodeReviewer`, and `Curator` using object-oriented programming (OOP) in Python.

All classes inherit from a base `Human` class, which defines a `name` property and a default `answer_question` method.

The `Student` class can ask questions to any `Human` object, while `Mentor`, `CodeReviewer`, and `Curator` override `answer_question` to provide specific responses for certain questions, falling back to the default response for unrecognized questions.

The main code creates instances and simulates interactions to produce the specified output, demonstrating polymorphism and inheritance.

## Purpose 🎯

Intended for educational purposes to illustrate OOP concepts such as inheritance, polymorphism, method overriding, and encapsulation, or for modeling interactions in a learning environment.

## How It Works 🔍

-   **Module Imports**:
    -   None required, as the code uses only built-in Python features.
-   **Human Class (Base)**:
    -   `__init__(name: str)`:
        -   Validates non-empty `name`.
        -   Sets `self.name`.
    -   `answer_question(question: str) -> None`:
        -   Prints default response: `"Very interesting question! I don't know."`.
-   **Student Class**:
    -   Inherits from `Human`.
    -   `ask_question(someone: Human, question: str) -> None`:
        -   Prints: `<someone.name>, <question>`.
        -   Calls `someone.answer_question(question.lower())` to ensure case-insensitive matching.
-   **Mentor Class**:
    -   Inherits from `Human`.
    -   Overrides `answer_question`:
        -   For `"i'm feeling sad, what should i do?"`: `"Take a rest and come back with questions about theory."`.
        -   For `"how can i get a job as a python engineer?"`: `"I'll tell you now."`.
        -   Else: Calls `super().answer_question(question)`.
-   **CodeReviewer Class**:
    -   Inherits from `Human`.
    -   Overrides `answer_question`:
        -   For `"what's wrong with my project?"`: `"Oh, a question about a project, that's what I love."`.
        -   Else: Calls `super().answer_question(question)`.
-   **Curator Class**:
    -   Inherits from `Human`.
    -   Overrides `answer_question`:
        -   For `"i'm feeling sad, what should i do?"`: `"Hold on, everything will work out. Do you want a video with cats?"`.
        -   Else: Calls `super().answer_question(question)`.
-   **Main Code**:
    -   Creates instances:
        -   `student = Student("Student")`.
        -   `marina = Curator("Marina")`.
        -   `ira = Mentor("Ira")`.
        -   `evgeny = CodeReviewer("Evgeny")`.
        -   `vitaly = Curator("Vitaly")`.
    -   Simulates interactions via `student.ask_question`:
        1. `marina`, `"I'm feeling sad, what should I do?"`.
        2. `ira`, `"I'm feeling sad, what should I do?"`.
        3. `evgeny`, `"when is the vacation?"`.
        4. `evgeny`, `"what's wrong with my project?"`.
        5. `vitaly`, `"how can I get a job as a Python engineer?"`.
        6. `ira`, `"how can I get a job as a Python engineer?"`.
-   **Behavior**:

    -   Produces exact output:

        ```
        Marina, I'm feeling sad, what should I do?
        Hold on, everything will work out. Do you want a video with cats?

        Ira, I'm feeling sad, what should I do?
        Take a rest and come back with questions about theory.

        Evgeny, when is the vacation?
        Very interesting question! I don't know.

        Evgeny, what's wrong with my project?
        Oh, a question about a project, that's what I love.

        Vitaly, how can I get a job as a Python engineer?
        Very interesting question! I don't know.

        Ira, how can I get a job as a Python engineer?
        I'll tell you now.
        ```

## Verification ✅

Implementation satisfies requirements:

-   **Functionality**:
    -   `Human` base class provides `name` and default `answer_question`.
    -   `Student` implements `ask_question` to print and delegate questions.
    -   `Mentor`, `CodeReviewer`, `Curator` override `answer_question` with specific responses.
    -   Produces exact output for all interactions.
-   **Correctness**:
    -   `ask_question` formats output as `<name>, <question>` and calls `answer_question`.
    -   Case-insensitive question matching (`question.lower()`).
    -   Specific responses match task requirements.
    -   Default response used for unrecognized questions.
    -   Name validation ensures non-empty names.
-   **Output**:
    -   Matches specified text exactly, including newlines and phrasing.
-   **Documentation**: Clear docstrings with type hints.

## Potential Considerations 🛠️

-   **Correctness**:
    -   `question.lower()` ensures robust matching (e.g., `"I'm feeling sad"` matches `"i'm feeling sad"`).
    -   `super().answer_question` correctly delegates to `Human` for unknown questions.
    -   Name validation prevents empty names.
    -   No validation for `question`, as any string is valid.
-   **Performance**:
    -   `ask_question`, `answer_question`: O(1) for string operations and printing.
    -   Total: O(1) per interaction, efficient for small-scale use.
-   **Design**:
    -   Inheritance hierarchy (`Human` → `Student`, etc.) models relationships clearly.
    -   Type hints (`str`, `'Human'`) clarify interfaces.
    -   Encapsulation via method-based question handling.
    -   Polymorphism allows different responses based on object type.
-   **Alternatives**:
    -   Dictionary-based responses: Less OOP, harder to extend.
    -   Single class with roles: Loses inheritance benefits.
    -   Case-sensitive matching: Less user-friendly.
-   **Extensibility**:
    -   Easily add new roles by inheriting from `Human`.
    -   Could add more question-response pairs.
    -   Could track question history or interaction logs.
-   **Edge Cases**:
    -   Empty question: Valid, handled by `answer_question`.
    -   Empty name: Prevented by `__init__` validation.
    -   Unknown question: Handled by default response.
    -   Same question to different roles: Handled by polymorphism.

## Usage Example (For Clarity, Not Submission) 📦

```python
# Provided example
student = Student("Student")
marina = Curator("Marina")
ira = Mentor("Ira")
evgeny = CodeReviewer("Evgeny")
vitaly = Curator("Vitaly")

student.ask_question(marina, "I'm feeling sad, what should I do?")
print()
student.ask_question(ira, "I'm feeling sad, what should I do?")
print()
student.ask_question(evgeny, "when is the vacation?")
print()
student.ask_question(evgeny, "what's wrong with my project?")
print()
student.ask_question(vitaly, "how can I get a job as a Python engineer?")
print()
student.ask_question(ira, "how can I get a job as a Python engineer?")
# Output:
# Marina, I'm feeling sad, what should I do?
# Hold on, everything will work out. Do you want a video with cats?
#
# Ira, I'm feeling sad, what should I do?
# Take a rest and come back with questions about theory.
#
# Evgeny, when is the vacation?
# Very interesting question! I don't know.
#
# Evgeny, what's wrong with my project?
# Oh, a question about a project, that's what I love.
#
# Vitaly, how can I get a job as a Python engineer?
# Very interesting question! I don't know.
#
# Ira, how can I get a job as a Python engineer?
# I'll tell you now.

# Additional test case
student.ask_question(marina, "What's the weather like?")
# Output:
# Marina, What's the weather like?
# Very interesting question! I don't know.
```

## Conclusion 🚀

The implementation successfully models the interaction between `Student`, `Mentor`, `CodeReviewer`, and `Curator` using an OOP hierarchy rooted in the `Human` class.

The `Student`’s `ask_question` method and overridden `answer_question` methods in derived classes produce the exact required output, demonstrating inheritance, polymorphism, and encapsulation.

The code is efficient, robust, and fully compliant with the task’s requirements, making it ideal for teaching OOP or simulating educational interactions.
