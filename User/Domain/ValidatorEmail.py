from .Validator import Validator
class EmailValidator(Validator):
    def __init__(self, email):
        self.email = email
        super().__init__()

    def isValid(self) -> bool:

        return True
