from .user_repository import UserRepository
from src.models.settings.db_connection_handler import db_connection_handler
def test_registry_user():
    db_connection_handler.get_connection()
    conn = db_connection_handler.get_connection()
    repo = UserRepository(conn)
    repo.registry_user('Euzinho'.lower(), '1234Mudar!')
    
def test_edit_name():
    db_connection_handler.get_connection()
    conn = db_connection_handler.get_connection()
    repo = UserRepository(conn)
    repo.edit_name(1, 'Euzinho222')
    
def test_edit_password():
    db_connection_handler.get_connection()
    conn = db_connection_handler.get_connection()
    repo = UserRepository(conn)
    repo.edit_password(1, '1234Mudar!222')
    

def test_get_user():
    db_connection_handler.get_connection()
    conn = db_connection_handler.get_connection()
    repo = UserRepository(conn)
    user = repo.get_user(1)
    print(user)    

def test_delete_user():
    db_connection_handler.get_connection()
    conn = db_connection_handler.get_connection()
    repo = UserRepository(conn)
    repo.delete_user(1)
    
