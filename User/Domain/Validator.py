from abc import ABC, abstractmethod
class Validator(ABC):
    @abstractmethod
    def isValid(self)-> bool:
        pass