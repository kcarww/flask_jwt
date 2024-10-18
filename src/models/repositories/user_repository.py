from pymysql import Connection
from src.models.interface.user_repository_interface import UserRepositoryInterface


class UserRepository(UserRepositoryInterface):
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn
        
    def registry_user(self, username: str, password: str) -> None:
        sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor = self.__conn.cursor()
        cursor.execute(sql, (username, password))
        self.__conn.commit()
        
    def edit_name(self, user_id: int, new_name: str) -> None:
        sql = "UPDATE users SET username = %s WHERE id = %s"
        cursor = self.__conn.cursor()
        cursor.execute(sql, (new_name, user_id))
        self.__conn.commit()
        
    def edit_password(self, user_id: int, new_password: str) -> None:
        sql = "UPDATE users SET password = %s WHERE id = %s"
        cursor = self.__conn.cursor()
        cursor.execute(sql, (new_password, user_id))
        self.__conn.commit()
        
    def delete_user(self, user_id: int) -> None:
        sql = "DELETE FROM users WHERE id = %s"
        cursor = self.__conn.cursor()
        cursor.execute(sql, (user_id,))
        self.__conn.commit()
        
    def get_user(self, user_id: int) -> dict:
        sql = "SELECT * FROM users WHERE id = %s"
        cursor = self.__conn.cursor()
        cursor.execute(sql, (user_id,))
        return cursor.fetchone()