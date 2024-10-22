from abc import ABC, abstractmethod
class UserRepositoryInterface(ABC):
    
        
    @abstractmethod
    def registry_user(self, username: str, password: str) -> None:
        pass
        
    @abstractmethod
    def edit_name(self, user_id: int, new_name: str) -> None:
        pass
        
    # @abstractmethod
    # def edit_password(self, user_id: int, new_password: str) -> None:
    #     pass
        
    # @abstractmethod
    # def delete_user(self, user_id: int) -> None:
    #     pass
        
    # @abstractmethod
    # def get_user(self, user_id: int) -> dict:
    #     pass
    
    # @abstractmethod
    # def get_user_by_username(self, username: str) -> dict:
    #     pass