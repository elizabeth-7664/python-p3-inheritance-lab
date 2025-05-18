
from user import User

class Student(User):  # 👈 Inherit from User
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)  # 👈 Use super to set names
        self.knowledge = []  # 👈 Students start with no knowledge

    def learn(self, string):
        self.knowledge.append(string)  # 👈 Add what the student learns
