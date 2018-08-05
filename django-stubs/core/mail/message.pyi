from email.mime.message import MIMEMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Any, Dict, List, Optional, Tuple, Union

from django.core.mail.backends.base import BaseEmailBackend

utf8_charset: Any
utf8_charset_qp: Any
DEFAULT_ATTACHMENT_MIME_TYPE: str
RFC5322_EMAIL_LINE_LENGTH_LIMIT: int

class BadHeaderError(ValueError): ...

ADDRESS_HEADERS: Any

def forbid_multi_line_headers(
    name: str, val: str, encoding: str
) -> Tuple[str, str]: ...
def split_addr(addr: str, encoding: str) -> Tuple[str, str]: ...
def sanitize_address(
    addr: Union[str, Tuple[str, str]], encoding: str
) -> str: ...

class MIMEMixin:
    def as_string(self, unixfrom: bool = ..., linesep: str = ...) -> str: ...
    def as_bytes(self, unixfrom: bool = ..., linesep: str = ...) -> bytes: ...

class SafeMIMEMessage(MIMEMixin, MIMEMessage):
    defects: List[Any]
    epilogue: None
    policy: email._policybase.Compat32
    preamble: None
    def __setitem__(self, name: str, val: str) -> None: ...

class SafeMIMEText(MIMEMixin, MIMEText):
    defects: List[Any]
    epilogue: None
    policy: email._policybase.Compat32
    preamble: None
    encoding: str = ...
    def __init__(
        self, _text: str, _subtype: str = ..., _charset: str = ...
    ) -> None: ...
    def __setitem__(self, name: str, val: str) -> None: ...
    def set_payload(self, payload: str, charset: str = ...) -> None: ...

class SafeMIMEMultipart(MIMEMixin, MIMEMultipart):
    defects: List[Any]
    epilogue: None
    policy: email._policybase.Compat32
    preamble: None
    encoding: str = ...
    def __init__(
        self,
        _subtype: str = ...,
        boundary: None = ...,
        _subparts: None = ...,
        encoding: str = ...,
        **_params: Any
    ) -> None: ...
    def __setitem__(self, name: str, val: str) -> None: ...

class EmailMessage:
    content_subtype: str = ...
    mixed_subtype: str = ...
    encoding: Any = ...
    to: List[str] = ...
    cc: List[Any] = ...
    bcc: List[Any] = ...
    reply_to: List[Any] = ...
    from_email: str = ...
    subject: str = ...
    body: str = ...
    attachments: List[Any] = ...
    extra_headers: Dict[Any, Any] = ...
    connection: None = ...
    def __init__(
        self,
        subject: str = ...,
        body: Optional[str] = ...,
        from_email: Optional[str] = ...,
        to: Optional[Union[List[str], str, Tuple[str, str]]] = ...,
        bcc: Optional[Union[str, List[str], Tuple[str]]] = ...,
        connection: Optional[BaseEmailBackend] = ...,
        attachments: Optional[
            Union[List[MIMEText], List[Tuple[str, str]]]
        ] = ...,
        headers: Optional[Dict[str, str]] = ...,
        cc: Optional[Union[str, List[str], Tuple[str, str]]] = ...,
        reply_to: Optional[Union[str, List[Union[str, None]]]] = ...,
    ) -> None: ...
    def get_connection(self, fail_silently: bool = ...) -> BaseEmailBackend: ...
    def message(self) -> MIMEMixin: ...
    def recipients(self) -> List[str]: ...
    def send(self, fail_silently: bool = ...) -> int: ...
    def attach(
        self,
        filename: Optional[Union[str, MIMEText]] = ...,
        content: Optional[Union[bytes, str, SafeMIMEText, EmailMessage]] = ...,
        mimetype: Optional[str] = ...,
    ) -> None: ...
    def attach_file(self, path: str, mimetype: Optional[str] = ...) -> None: ...

class EmailMultiAlternatives(EmailMessage):
    attachments: List[Any]
    bcc: List[Any]
    body: django.utils.safestring.SafeText
    cc: List[Any]
    connection: None
    extra_headers: Dict[Any, Any]
    from_email: str
    reply_to: List[Any]
    subject: str
    to: List[str]
    alternative_subtype: str = ...
    alternatives: Any = ...
    def __init__(
        self,
        subject: str = ...,
        body: str = ...,
        from_email: Optional[str] = ...,
        to: Optional[List[str]] = ...,
        bcc: Optional[List[str]] = ...,
        connection: Optional[BaseEmailBackend] = ...,
        attachments: None = ...,
        headers: Optional[Dict[str, str]] = ...,
        alternatives: Optional[List[Tuple[str, str]]] = ...,
        cc: None = ...,
        reply_to: None = ...,
    ) -> None: ...
    def attach_alternative(self, content: str, mimetype: str) -> None: ...
