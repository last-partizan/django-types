from typing import Any, Callable, Dict, List, Optional, Tuple, Type, Union

from django.core.cache.backends.base import BaseCache


class DummyCache(BaseCache):
    default_timeout: int
    key_func: Callable
    key_prefix: str
    version: int
    def __init__(self, host: str, *args: Any, **kwargs: Any) -> None: ...
    def add(
        self, key: str, value: str, timeout: Any = ..., version: None = ...
    ) -> bool: ...
    def get(
        self,
        key: str,
        default: Optional[str] = ...,
        version: Optional[int] = ...,
    ) -> Optional[str]: ...
    def set(
        self,
        key: str,
        value: Union[
            str,
            Dict[
                str,
                Union[
                    str,
                    int,
                    List[int],
                    Tuple[int, int, int, int],
                    Dict[str, int],
                    Callable,
                    Type[Any],
                ],
            ],
            int,
        ],
        timeout: Any = ...,
        version: Optional[str] = ...,
    ) -> None: ...
    def touch(
        self, key: str, timeout: Any = ..., version: None = ...
    ) -> bool: ...
    def delete(self, key: str, version: None = ...) -> None: ...
    def has_key(self, key: str, version: None = ...) -> bool: ...
    def clear(self) -> None: ...
