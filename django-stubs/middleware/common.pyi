from typing import Any, Optional

from django.core.handlers.wsgi import WSGIRequest
from django.http.request import HttpRequest
from django.http.response import (HttpResponseBase, HttpResponseNotFound,
                                  HttpResponsePermanentRedirect)
from django.utils.deprecation import MiddlewareMixin


class CommonMiddleware(MiddlewareMixin):
    get_response: Optional[Callable]
    response_redirect_class: Any = ...
    def process_request(
        self, request: WSGIRequest
    ) -> Optional[HttpResponsePermanentRedirect]: ...
    def should_redirect_with_slash(self, request: WSGIRequest) -> bool: ...
    def get_full_path_with_slash(self, request: WSGIRequest) -> str: ...
    def process_response(
        self, request: HttpRequest, response: HttpResponseBase
    ) -> HttpResponseBase: ...

class BrokenLinkEmailsMiddleware(MiddlewareMixin):
    get_response: None
    def process_response(
        self, request: WSGIRequest, response: HttpResponseNotFound
    ) -> HttpResponseNotFound: ...
    def is_internal_request(self, domain: str, referer: str) -> bool: ...
    def is_ignorable_request(
        self, request: WSGIRequest, uri: str, domain: str, referer: str
    ) -> bool: ...
