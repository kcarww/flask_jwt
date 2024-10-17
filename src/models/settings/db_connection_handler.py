import pymysql.cursors
from pymysql.connections import Connection

class __DbConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = {
            'host': 'localhost',
            'user': 'root',
            'password': '',
            'db': 'db__flask',
            'cursorclass': pymysql.cursors.DictCursor
        }
        self.__conn = None
        
        
    def connect(self) -> None:
        self.__conn = pymysql.connect(**self.__connection_string)
    
    def get_connection(self) -> Connection:
        self.connect()
        return self.__conn
    


db_connection_handler = __DbConnectionHandler()    