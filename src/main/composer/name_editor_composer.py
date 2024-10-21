from src.models.settings.db_connection_handler import db_connection_handler
from src.models.repositories.user_repository import UserRepository
from src.controllers.name_editor import NameEditor
from src.views.name_editor import NameEditorView
def name_editor_composer():
    conn = db_connection_handler.get_connection()
    model = UserRepository(conn)
    controller = NameEditor(model)
    view = NameEditorView(controller)
    return view
