from User.Domain.Validator import Validator

class ValidatorUsername(Validator):
    def __init__(self, username):
        self.username = username

    def isValid(self)-> bool:
        if len(self.username) < 3:
            raise ValueError("Username must be at least 3 characters long.")
        return True