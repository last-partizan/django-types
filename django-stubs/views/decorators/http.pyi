from typing import Any, Callable, List, Optional

conditional_page: Any

def require_http_methods(request_method_list: List[str]) -> Callable: ...

require_GET: Any
require_POST: Any
require_safe: Any

def condition(
    etag_func: Optional[Callable] = ...,
    last_modified_func: Optional[Callable] = ...,
) -> Callable: ...
def etag(etag_func: Callable) -> Callable: ...
def last_modified(last_modified_func: Callable) -> Callable: ...
