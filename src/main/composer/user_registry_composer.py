from src.models.settings.db_connection_handler import db_connection_handler
from src.models.repositories.user_repository import UserRepository
from src.controllers.user_registry import UserRegistry
from src.views.user_registry_view import UserRegisterView

def user_registry_composer():
    conn = db_connection_handler.get_connection()
    model = UserRepository(conn)
    controller = UserRegistry(model)
    view = UserRegisterView(controller)
    return view