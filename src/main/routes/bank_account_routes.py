from flask import Blueprint, jsonify, request
from src.main.composer.user_registry_composer import user_registry_composer
from src.main.composer.login_creator_composer import login_creator_composer
from src.main.composer.name_editor_composer import name_editor_composer
from src.views.http_types.http_request import HttpRequest
bank_routes_bp = Blueprint('bank_routes', __name__)

@bank_routes_bp.route("/bank/registry", methods=['POST'])
def registry_user():
    http_request = HttpRequest(body=request.json)
    http_response = user_registry_composer().handle(http_request)
    return jsonify(http_response.body), http_response.status_code



@bank_routes_bp.route("/bank/login", methods=['POST'])
def create_login():
    http_request = HttpRequest(body=request.json)
    http_response = login_creator_composer().handle(http_request)
    return jsonify(http_response.body), http_response.status_code


@bank_routes_bp.route("/bank/name/<user_id>", methods=['PUT'])
def edit_name(user_id):
    http_request = HttpRequest(body=request.json, params={'user_id': user_id})
    http_response = name_editor_composer().handle(http_request)
    return jsonify(http_response.body), http_response.status_code