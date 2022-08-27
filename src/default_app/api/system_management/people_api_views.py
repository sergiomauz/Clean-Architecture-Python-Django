"""
    ToDo: DocString
"""
import uuid
from mediatr import Mediator
from rest_framework.response import Response
from rest_framework.decorators import api_view
from common_library.utils import Constants
from default_app.api.common import ApiResponseVm
from default_app.use_cases.system_management.people.commands.create_person import (
    CreatePersonCommand, CreatePersonVm, CreatePersonHandler)
from default_app.use_cases.system_management.people.queries.get_person import (
    GetPersonQuery, GetPersonVm, GetPersonHandler)
from default_app.use_cases.system_management.people.queries.search_people import (
    SearchPeopleQuery, SearchPeopleVm, SearchPeopleHandler)
from default_app.use_cases.system_management.people.commands.update_person import (
    UpdatePersonCommand, UpdatePersonVm, UpdatePersonHandler)
from default_app.use_cases.system_management.people.commands.delete_person import (
    DeletePersonCommand, DeletePersonVm, DeletePersonHandler)


@api_view(["POST", "GET", "PUT", "DELETE"])
def people_crud_api_view(request) -> Response:
    """ ToDo: DocString """
    mediator = Mediator()
    response = None
    if request.method == "POST":
        command = CreatePersonCommand.new(request)
        application_view_model = mediator.send(command)
        api_response_view_model = ApiResponseVm(application_view_model)

        response = Response(
            api_response_view_model.json_object,
            status = api_response_view_model.result.status_code,
            content_type = Constants.CONTENT_TYPE_JSON
        )

    elif request.method == "GET":
        query = SearchPeopleQuery.new(request)
        application_view_model = mediator.send(query)
        api_response_view_model = ApiResponseVm(application_view_model)

        response = Response(
            api_response_view_model.json_object,
            status = api_response_view_model.result.status_code,
            content_type = Constants.CONTENT_TYPE_JSON
        )

    elif request.method == "PUT":
        command = UpdatePersonCommand.new(request)
        application_view_model = mediator.send(command)
        api_response_view_model = ApiResponseVm(application_view_model)

        response = Response(
            api_response_view_model.json_object,
            status = api_response_view_model.result.status_code,
            content_type = Constants.CONTENT_TYPE_JSON
        )

    elif request.method == "DELETE":
        command = DeletePersonCommand.new(request)
        application_view_model = mediator.send(command)
        api_response_view_model = ApiResponseVm(application_view_model)

        response = Response(
            api_response_view_model.json_object,
            status = api_response_view_model.result.status_code,
            content_type = Constants.CONTENT_TYPE_JSON
        )

    return response


@api_view(["GET"])
def person_read_api_view(request, uid: uuid) -> Response:
    """ ToDo: DocString """
    mediator = Mediator()
    response = None
    if request.method == "GET":
        query = GetPersonQuery.new(uid)
        application_view_model = mediator.send(query)
        api_response_view_model = ApiResponseVm(application_view_model)

        response = Response(
            api_response_view_model.json_object,
            status = api_response_view_model.result.status_code,
            content_type = Constants.CONTENT_TYPE_JSON
        )

    return response
