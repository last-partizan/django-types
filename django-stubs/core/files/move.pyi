from typing import Any, Optional


def file_move_safe(
    old_file_name: str,
    new_file_name: str,
    chunk_size: int = ...,
    allow_overwrite: bool = ...,
) -> None: ...
