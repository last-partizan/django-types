from typing import Any, Dict, Optional

from django.contrib.sessions.backends.db import SessionStore as DBStore

KEY_PREFIX: str

class SessionStore(DBStore):
    accessed: bool
    modified: bool
    serializer: Type[django.core.signing.JSONSerializer]
    cache_key_prefix: Any = ...
    def __init__(self, session_key: Optional[str] = ...) -> None: ...
    @property
    def cache_key(self) -> str: ...
    def load(self) -> Dict[str, str]: ...
    def exists(self, session_key: Optional[str]) -> bool: ...
    def save(self, must_create: bool = ...) -> None: ...
    def delete(self, session_key: Optional[str] = ...) -> None: ...
    def flush(self) -> None: ...
