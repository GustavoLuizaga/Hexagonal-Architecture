from User.Domain.UserRepository import UserRepository
from User.Domain.User import User
from .PostgreUserModel import PostgreUser

class PostgreUserRepository(UserRepository):

    def saveUser(self, user: User) -> User:
        postgreUser = PostgreUser(username=user.get_username(), email=user.get_email(), password=user.get_password())
        postgreUser.save()
        return user

    def searchUserGmail(self, gmail:str) -> User:
        postgreUser = PostgreUser.objects.get(username=gmail)
        user = User(first_name="", last_name="", username=postgreUser.username, email=postgreUser.email,password=postgreUser.password)
        return user