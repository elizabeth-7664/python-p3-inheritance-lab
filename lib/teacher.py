# lib/teacher.py
import random
from user import User  # Make sure to import User class

knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]

class Teacher(User):  # 👈 Inherit from User
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)  # 👈 Call the parent’s __init__
        self.knowledge = knowledge  # 👈 Set up the knowledge list

    def teach(self):
        index = random.randint(0, len(self.knowledge) - 1)
        return self.knowledge[index]
