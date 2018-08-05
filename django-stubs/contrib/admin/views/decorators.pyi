from typing import Any, Callable, Optional


def staff_member_required(
    view_func: Optional[Callable] = ...,
    redirect_field_name: str = ...,
    login_url: str = ...,
) -> Callable: ...
