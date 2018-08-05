from datetime import datetime
from typing import Any, Optional, Union

from django.template import Node
from django.template.base import FilterExpression, NodeList, Parser, Token
from django.template.context import Context
from django.utils.safestring import SafeText
from django.utils.timezone import FixedOffset

register: Any

class datetimeobject(datetime): ...

def localtime(
    value: Optional[Union[str, datetime]]
) -> Union[str, datetimeobject]: ...
def utc(
    value: Optional[Union[str, datetime]]
) -> Union[str, datetimeobject]: ...
def do_timezone(
    value: Optional[Union[str, datetime]],
    arg: Optional[Union[str, FixedOffset]],
) -> Union[str, datetimeobject]: ...

class LocalTimeNode(Node):
    origin: django.template.base.Origin
    token: django.template.base.Token
    nodelist: django.template.base.NodeList = ...
    use_tz: bool = ...
    def __init__(self, nodelist: NodeList, use_tz: bool) -> None: ...
    def render(self, context: Context) -> SafeText: ...

class TimezoneNode(Node):
    origin: django.template.base.Origin
    token: django.template.base.Token
    nodelist: django.template.base.NodeList = ...
    tz: django.template.base.FilterExpression = ...
    def __init__(self, nodelist: NodeList, tz: FilterExpression) -> None: ...
    def render(self, context: Context) -> SafeText: ...

class GetCurrentTimezoneNode(Node):
    origin: django.template.base.Origin
    token: django.template.base.Token
    variable: str = ...
    def __init__(self, variable: str) -> None: ...
    def render(self, context: Context) -> str: ...

def localtime_tag(parser: Parser, token: Token) -> LocalTimeNode: ...
def timezone_tag(parser: Parser, token: Token) -> TimezoneNode: ...
def get_current_timezone_tag(
    parser: Parser, token: Token
) -> GetCurrentTimezoneNode: ...
