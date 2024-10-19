from src.controllers.interfaces.name_editor import NameEditorInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface

class NameEditorView(ViewInterface):
    def __init__(self, controller: NameEditorInterface):
        self.__controller = controller
        
    def handle(self, request: HttpRequest) -> HttpResponse:
        new_name = request.body.get('new_name')
        user_id = request.params.get('user_id')
        response = self.__controller.edit(user_id, new_name)
        return HttpResponse(
            body= {
                "data": response
            },
            status_code=200
        )