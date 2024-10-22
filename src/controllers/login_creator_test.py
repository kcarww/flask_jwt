from src.drivers.password_handler import PasswordHandler
from .login_creator import LoginCreator


username = "meuUsername"
password = "minhaSenha"

hashed_password = PasswordHandler().encrypt_password(password)


class MockUserRepository:
    def get_user_by_username(self, username):
        return {"id": 10, "username": username, "password": hashed_password}

def test_login_creator():
    login_creator = LoginCreator(MockUserRepository())
    response = login_creator.create(username, password)
    
    print()
    print(response)
    
    assert response["access"] is True
    assert response["username"] == username
    assert response["token"] is not None