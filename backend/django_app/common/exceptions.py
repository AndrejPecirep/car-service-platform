from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status


class ServiceException(Exception):
    """
    Custom business exception
    """

    def __init__(self, message, code=status.HTTP_400_BAD_REQUEST):
        self.message = message
        self.code = code
        super().__init__(message)


def custom_exception_handler(exc, context):
    """
    Global DRF exception handler
    """
    response = exception_handler(exc, context)

    if response is not None:
        return response

    if isinstance(exc, ServiceException):
        return Response(
            {"error": exc.message},
            status=exc.code
        )

    return Response(
        {"error": "Internal server error"},
        status=status.HTTP_500_INTERNAL_SERVER_ERROR
    )