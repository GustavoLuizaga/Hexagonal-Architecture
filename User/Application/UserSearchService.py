from User.Domain.UserRepository import UserRepository
from User.Domain.User import User

class UserSearchService:
    def __init__(self):
        self.userRepository = UserRepository()

    def searchUser(self, gmail:str) -> User:
        return self.userRepository.searchUserGmail(gmail)
