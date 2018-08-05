from typing import Any, Callable, Dict, Optional, Tuple

from django.core.handlers.wsgi import WSGIRequest
from django.http.response import HttpResponse
from django.utils.deprecation import MiddlewareMixin

from .utils import get_view_name


class XViewMiddleware(MiddlewareMixin):
    get_response: None
    def process_view(
        self,
        request: WSGIRequest,
        view_func: Callable,
        view_args: Tuple,
        view_kwargs: Dict[Any, Any],
    ) -> Optional[HttpResponse]: ...
