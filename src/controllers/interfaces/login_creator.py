from abc import ABC, abstractmethod

class LoginCreatorInterface(ABC):
    @abstractmethod
    def create(self, username: str, password: str) -> dict:
        pass