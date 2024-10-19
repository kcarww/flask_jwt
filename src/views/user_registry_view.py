from .interfaces.view_interface import ViewInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.interfaces.user_registry import UserRegisterInterface

class UserRegisterView(ViewInterface):
    def __init__(self, controller: UserRegisterInterface):
        self.__controller = controller
        
    def handle(self, request: HttpRequest) -> HttpResponse:
        username = request.body['username']
        password = request.body['password']
        response = self.__controller.registry(username, password)
        return HttpResponse(
            body= {
                "data": response
            },
            status_code=201
        )