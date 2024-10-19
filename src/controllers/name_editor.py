from src.controllers.interfaces.name_editor import NameEditorInterface
from src.models.interface.user_repository_interface import UserRepositoryInterface


class NameEditor(NameEditorInterface):
    def __init__(self, user_repository: UserRepositoryInterface):
        self.__user_repository = user_repository
        
        
    def edit(self, user_id: int, new_name: str) -> None:
        self.__user_repository.edit_name(user_id, new_name)
        return {
            "type": "User",
            "count": 1,
            "new name": new_name
        }