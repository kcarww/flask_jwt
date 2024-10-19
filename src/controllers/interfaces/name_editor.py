from abc import ABC, abstractmethod

class NameEditorInterface(ABC):
    @abstractmethod
    def edit(self, user_id: int, new_name: str) -> str:
        pass