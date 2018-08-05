from typing import Any, Callable, List, Optional, Union

USE_INOTIFY: bool
fd: Any
RUN_RELOADER: bool
FILE_MODIFIED: int
I18N_MODIFIED: int

def gen_filenames(only_new: bool = ...) -> List[str]: ...
def clean_files(
    filelist: Union[List[Union[None, bool]], List[Union[str, None]]]
) -> List[str]: ...
def reset_translations() -> None: ...
def inotify_code_changed(): ...
def code_changed(): ...
def check_errors(fn: Callable) -> Callable: ...
def raise_last_exception() -> None: ...
def ensure_echo_on() -> None: ...
def reloader_thread() -> None: ...
def restart_with_reloader() -> int: ...
def python_reloader(main_func: Any, args: Any, kwargs: Any) -> None: ...
def main(
    main_func: Any, args: Optional[Any] = ..., kwargs: Optional[Any] = ...
) -> None: ...
