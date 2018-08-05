from typing import Any, Callable, Optional, Type

from django.http.request import HttpRequest
from django.http.response import HttpResponseBase


class RemovedInDjango30Warning(PendingDeprecationWarning): ...
class RemovedInNextVersionWarning(DeprecationWarning): ...

class warn_about_renamed_method:
    class_name: str = ...
    old_method_name: str = ...
    new_method_name: str = ...
    deprecation_warning: Type[DeprecationWarning] = ...
    def __init__(
        self,
        class_name: str,
        old_method_name: str,
        new_method_name: str,
        deprecation_warning: Type[DeprecationWarning],
    ) -> None: ...
    def __call__(self, f: Callable) -> Callable: ...

class RenameMethodsBase(type):
    renamed_methods: Any = ...
    def __new__(cls, name: Any, bases: Any, attrs: Any): ...

class DeprecationInstanceCheck(type):
    alternative: str
    deprecation_warning: Type[
        django.utils.deprecation.RemovedInNextVersionWarning
    ]
    def __instancecheck__(self, instance: Any): ...

class MiddlewareMixin:
    get_response: Any = ...
    def __init__(self, get_response: Optional[Callable] = ...) -> None: ...
    def __call__(self, request: HttpRequest) -> HttpResponseBase: ...
