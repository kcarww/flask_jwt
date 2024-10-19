from abc import ABC, abstractmethod

class UserRegisterInterface(ABC):
    @abstractmethod
    def registry(self, username: str, password: str) -> dict:
        pass