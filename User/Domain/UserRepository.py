from abc import ABC, abstractmethod
from .User import User
class UserRepository(ABC):
    @abstractmethod
    def saveUser(self, user:User) -> User:
        pass

    @abstractmethod
    def searchUserGmail(self, gmail:str) -> User:
        pass