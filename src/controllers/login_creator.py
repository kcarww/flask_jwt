from src.controllers.interfaces.login_creator import LoginCreatorInterface
from src.models.interface.user_repository_interface import UserRepositoryInterface
from src.drivers.jwt_handler import JwtHandler
from src.drivers.password_handler import PasswordHandler

class LoginCreator(LoginCreatorInterface):
    def __init__(self, user_repository: UserRepositoryInterface):
        self.__user_repository = user_repository
        self.__jwt_handler = JwtHandler()
        self.__password_handler = PasswordHandler()
        
        
    def create(self, username: str, password: str) -> dict:
        user = self.__find_user(username)
        user_id = user['id']
        hashed_password = user['password']
        self.__verify_correct_password(password, hashed_password)
        token = self.__create_jwt_token(user_id)
        return self.__format_response(username, token)
        
    
    def __find_user(self, username: str) -> dict:
        user = self.__user_repository.get_user_by_username(username)
        if not user:
            raise Exception("User not found")
        
        return user
    
    def __verify_correct_password(self, password: str, hashed_password: str) -> None:
        if not self.__password_handler.verify_password(password, hashed_password):
            raise Exception("Incorrect password")
        
    def __create_jwt_token(self, user_id: int) -> str:
        payload = {"user_id": user_id}
        return self.__jwt_handler.create_jwt_token(payload)
    
    def __format_response(self, username: str, token: str) -> dict:
        return {
            "access": True,
            "username": username,
            "token": token
        }