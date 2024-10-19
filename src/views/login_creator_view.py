from .interfaces.view_interface import ViewInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.interfaces.login_creator import LoginCreatorInterface

class LoginCreatorView(ViewInterface):
    def __init__(self, controller: LoginCreatorInterface):
        self.__controller = controller
        
    def handle(self, request: HttpRequest) -> HttpResponse:
        username = request.body['username']
        password = request.body['password']
        response = self.__controller.create(username, password)
        return HttpResponse(
            body= {
                "data": response
            },
            status_code=200
        )