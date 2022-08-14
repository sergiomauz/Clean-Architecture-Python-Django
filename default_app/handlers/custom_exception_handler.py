"""
    ToDo: DocString
"""
from mediatr import Mediator
from rest_framework.response import Response
from common_library.utils import Constants
from default_app.api.common import ApiResponseVm
from default_app.use_cases.system_management.errors_log.commands.create_error_log import (
    CreateErrorLogCommand, CreateErrorLogVm, CreateErrorLogHandler)


def custom_exception_handler(exception, context) -> Response:
    """ ToDo: DocString """
    mediator = Mediator()
    command = CreateErrorLogCommand(exception, context)
    error_view_model = mediator.send(command)
    api_response_view_model = ApiResponseVm(error_view_model)

    return Response(
        api_response_view_model.json_object,
        status = api_response_view_model.result.status_code,
        content_type = Constants.CONTENT_TYPE_JSON)
