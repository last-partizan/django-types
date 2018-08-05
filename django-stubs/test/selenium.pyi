from typing import Any, Callable, Dict, List, Optional, Tuple, Type, Union

from django.test import LiveServerTestCase


class SeleniumTestCaseBase:
    browsers: Any = ...
    browser: Any = ...
    def __new__(
        cls: Type[SeleniumTestCaseBase],
        name: str,
        bases: Tuple[Type[SeleniumTestCase]],
        attrs: Dict[str, Union[str, List[str], Callable]],
    ) -> Type[SeleniumTestCase]: ...
    @classmethod
    def import_webdriver(cls, browser: Any): ...
    def create_webdriver(self): ...

class SeleniumTestCase(LiveServerTestCase):
    implicit_wait: int = ...
    @classmethod
    def setUpClass(cls) -> None: ...
    def disable_implicit_wait(self) -> None: ...
