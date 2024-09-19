from User.Domain.User import User
from User.Domain.ValidatorUsername import ValidatorUsername
from User.Domain.ValidatorEmail import  EmailValidator
from User.Domain.UserRepository import UserRepository


class UserRegistrationService:
    def __init__(self,userRepository:UserRepository):
        self.userRepository = userRepository
    #VALIDA LOS CAMPOS Y LE PASAMOS COMO PARAMETRO EL PASSWORD

    def registerUser(self,username:str,email:str,password:int) -> User:
        validatorEmail = EmailValidator(email)
        validatorUsername = ValidatorUsername(username)
        validatorUsername.isValid()
        validatorEmail.isValid()


        user = User(first_name="", last_name="", username=username, email=email,password=password)

        # Guardar el usuario en el repositorio
        return self.userRepository.saveUser(user)
