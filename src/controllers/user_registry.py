from src.models.interface.user_repository_interface import UserRepositoryInterface
from src.drivers.password_handler import PasswordHandler

class UserRegistry(UserRepositoryInterface):
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.repo = user_repository
        self.__password_handler = PasswordHandler()
        
    def registry(self, username: str, password: str) -> dict:
        hashed_password = self.__create_hash_password(password)
        self.repo.registry_user(username, hashed_password)
        return self.__format_response(username) 
        
        
    def __create_hash_password(self, password: str) -> str:
        hashed_password = self.__password_handler.encrypt_password(password)
        return hashed_password
    
    def __format_response(self, username: str) -> dict:
        return {
            "type": "User",
            "count": 1,
            "username": username
        }
        
    def edit_name(self, user_id: int, new_name: str) -> None:
        pass
    
    def registry_user(self, username: str, password: str) -> None:
        pass