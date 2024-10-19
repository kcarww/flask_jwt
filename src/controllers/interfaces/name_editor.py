from abc import ABC, abstractmethod

class NameEditorInterface(ABC):
    @abstractmethod
    def edit(self, name: str) -> str:
        pass