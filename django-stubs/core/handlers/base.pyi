from typing import Any, Callable, Optional

from django.core.handlers.wsgi import WSGIRequest
from django.http.response import HttpResponse, HttpResponseBase

from .exception import convert_exception_to_response, get_exception_response

logger: Any

class BaseHandler:
    def load_middleware(self) -> None: ...
    def make_view_atomic(self, view: Callable) -> Callable: ...
    def get_exception_response(
        self, request: Any, resolver: Any, status_code: Any, exception: Any
    ): ...
    def get_response(self, request: WSGIRequest) -> HttpResponseBase: ...
    def process_exception_by_middleware(
        self, exception: Exception, request: WSGIRequest
    ) -> HttpResponse: ...
