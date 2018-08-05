from typing import Any, Callable, List, Optional

from django.db.backends.sqlite3.schema import DatabaseSchemaEditor
from django.db.migrations.operations.models import CreateModel
from django.db.migrations.state import ProjectState, StateApps

from .base import Operation


class SeparateDatabaseAndState(Operation):
    serialization_expand_args: Any = ...
    database_operations: Any = ...
    state_operations: Any = ...
    def __init__(
        self,
        database_operations: List[Any] = ...,
        state_operations: List[CreateModel] = ...,
    ) -> None: ...
    def deconstruct(self): ...
    def state_forwards(self, app_label: str, state: ProjectState) -> None: ...
    def database_forwards(
        self,
        app_label: str,
        schema_editor: DatabaseSchemaEditor,
        from_state: ProjectState,
        to_state: ProjectState,
    ) -> None: ...
    def database_backwards(
        self,
        app_label: str,
        schema_editor: DatabaseSchemaEditor,
        from_state: ProjectState,
        to_state: ProjectState,
    ) -> None: ...
    def describe(self): ...

class RunSQL(Operation):
    noop: str = ...
    sql: Any = ...
    reverse_sql: Any = ...
    state_operations: Any = ...
    hints: Any = ...
    elidable: Any = ...
    def __init__(
        self,
        sql: Any,
        reverse_sql: Optional[Any] = ...,
        state_operations: Optional[Any] = ...,
        hints: Optional[Any] = ...,
        elidable: bool = ...,
    ) -> None: ...
    def deconstruct(self): ...
    @property
    def reversible(self): ...
    def state_forwards(self, app_label: Any, state: Any) -> None: ...
    def database_forwards(
        self, app_label: Any, schema_editor: Any, from_state: Any, to_state: Any
    ) -> None: ...
    def database_backwards(
        self, app_label: Any, schema_editor: Any, from_state: Any, to_state: Any
    ) -> None: ...
    def describe(self): ...

class RunPython(Operation):
    reduces_to_sql: bool = ...
    atomic: Any = ...
    code: Any = ...
    reverse_code: Any = ...
    hints: Any = ...
    elidable: Any = ...
    def __init__(
        self,
        code: Callable,
        reverse_code: Optional[Callable] = ...,
        atomic: Optional[bool] = ...,
        hints: None = ...,
        elidable: bool = ...,
    ) -> None: ...
    def deconstruct(self): ...
    @property
    def reversible(self) -> bool: ...
    def state_forwards(self, app_label: str, state: ProjectState) -> None: ...
    def database_forwards(
        self,
        app_label: str,
        schema_editor: DatabaseSchemaEditor,
        from_state: ProjectState,
        to_state: ProjectState,
    ) -> None: ...
    def database_backwards(
        self,
        app_label: str,
        schema_editor: DatabaseSchemaEditor,
        from_state: ProjectState,
        to_state: ProjectState,
    ) -> None: ...
    def describe(self): ...
    @staticmethod
    def noop(apps: StateApps, schema_editor: DatabaseSchemaEditor) -> None: ...
