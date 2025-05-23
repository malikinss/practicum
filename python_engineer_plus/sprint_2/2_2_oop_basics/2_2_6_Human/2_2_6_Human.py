'''
TODO:
    Describe the interaction between a student, mentor, code reviewer,
    and curator in OOP.

    All of these people are people, so let's create a base class Human with
    a name property (every person should have a name)
    and an answer_question() method for answering questions.

    By default, the Human object will answer any question like this:
        "Very interesting question! I don't know."

    Let's inherit the Student, Mentor, CodeReviewer, and Curator classes from
    the Human class.

    A student should be able to ask questions.

    Implement the ask_question(Human, question) method in the Student class.

    When called, this method should:
        1. Print the question on the screen in the format:
            <name of the person to whom we are asking the question>,
            <text of the question>
        2. Ask the question to the person, an object of the Human class.
           The name of the object to which the question is addressed is passed
           when calling the ask_question() method.

    Mentor, CodeReviewer, and Curator class objects should be able to answer
    questions when the answer_question() method is called.

    An unexpected question was asked — the default answer will do.

    After you finish writing the code, your program should display
    the following text on the screen:
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
'''


class Human:
    """
    Base class for people with a name and question-answering ability.
    """

    def __init__(self, name: str) -> None:
        """
        Initialize a person with a name.

        Args:
            name: Person's name.

        Raises:
            ValueError: If name is empty.
        """
        if not name:
            raise ValueError("Name cannot be empty")
        self.name = name

    def answer_question(self, question: str) -> None:
        """
        Answer a question with a default response.

        Args:
            question: The question asked.

        Returns:
            None, prints the response.
        """
        print("Very interesting question! I don't know.")


class Student(Human):
    """
    A student who can ask questions to other people.
    """

    def ask_question(self, someone: 'Human', question: str) -> None:
        """
        Ask a question to another person.

        Args:
            someone: The person to ask.
            question: The question to ask.

        Returns:
            None, prints the question and answer.
        """
        print(f"{someone.name}, {question}")
        someone.answer_question(question.lower())


class Mentor(Human):
    """
    A mentor who answers specific questions about learning and careers.
    """

    def answer_question(self, question: str) -> None:
        """
        Answer questions about learning or careers.

        Args:
            question: The question asked.

        Returns:
            None, prints the response.
        """
        question = question.lower()
        if question == "i'm feeling sad, what should i do?":
            print("Take a rest and come back with questions about theory.")
        elif question == "how can i get a job as a python engineer?":
            print("I'll tell you now.")
        else:
            super().answer_question(question)


class CodeReviewer(Human):
    """
    A code reviewer who answers questions about projects.
    """

    def answer_question(self, question: str) -> None:
        """
        Answer questions about projects.

        Args:
            question: The question asked.

        Returns:
            None, prints the response.
        """
        question = question.lower()
        if question == "what's wrong with my project?":
            print("Oh, a question about a project, that's what I love.")
        else:
            super().answer_question(question)


class Curator(Human):
    """
    A curator who provides emotional support and answers questions.
    """

    def answer_question(self, question: str) -> None:
        """
        Answer questions with emotional support.

        Args:
            question: The question asked.

        Returns:
            None, prints the response.
        """
        question = question.lower()
        if question == "i'm feeling sad, what should i do?":
            print(
                "Hold on, everything will work out. "
                "Do you want a video with cats?"
            )
        else:
            super().answer_question(question)


# Create people
student = Student("Student")
marina = Curator("Marina")
ira = Mentor("Ira")
evgeny = CodeReviewer("Evgeny")
vitaly = Curator("Vitaly")

# Simulate interactions
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
