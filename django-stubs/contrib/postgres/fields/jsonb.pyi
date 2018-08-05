from typing import Any, Dict, List, Optional, Tuple, Type, Union

from psycopg2.extras import Json

from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Field, Transform
from django.db.models import lookups as builtin_lookups

from .mixins import CheckFieldDefaultMixin


class JsonAdapter(Json):
    encoder: Any = ...
    def __init__(
        self,
        adapted: Any,
        dumps: Optional[Any] = ...,
        encoder: Optional[Any] = ...,
    ) -> None: ...
    def dumps(self, obj: Any): ...

class JSONField(CheckFieldDefaultMixin, Field):
    empty_strings_allowed: bool = ...
    description: Any = ...
    default_error_messages: Any = ...
    encoder: Any = ...
    def __init__(
        self,
        verbose_name: None = ...,
        name: None = ...,
        encoder: Optional[Type[DjangoJSONEncoder]] = ...,
        **kwargs: Any
    ) -> None: ...
    def db_type(self, connection: Any): ...
    def deconstruct(
        self
    ) -> Tuple[
        None, str, List[Any], Dict[str, Union[bool, Type[DjangoJSONEncoder]]]
    ]: ...
    def get_transform(self, name: Any): ...
    def get_prep_value(self, value: Any): ...
    def validate(self, value: Any, model_instance: Any) -> None: ...
    def value_to_string(self, obj: Any): ...
    def formfield(self, **kwargs: Any): ...

class KeyTransform(Transform):
    operator: str = ...
    nested_operator: str = ...
    key_name: Any = ...
    def __init__(self, key_name: Any, *args: Any, **kwargs: Any) -> None: ...
    def as_sql(self, compiler: Any, connection: Any): ...

class KeyTextTransform(KeyTransform):
    operator: str = ...
    nested_operator: str = ...
    output_field: Any = ...

class KeyTransformTextLookupMixin:
    def __init__(
        self, key_transform: Any, *args: Any, **kwargs: Any
    ) -> None: ...

class KeyTransformIExact(
    KeyTransformTextLookupMixin, builtin_lookups.IExact
): ...
class KeyTransformIContains(
    KeyTransformTextLookupMixin, builtin_lookups.IContains
): ...
class KeyTransformStartsWith(
    KeyTransformTextLookupMixin, builtin_lookups.StartsWith
): ...
class KeyTransformIStartsWith(
    KeyTransformTextLookupMixin, builtin_lookups.IStartsWith
): ...
class KeyTransformEndsWith(
    KeyTransformTextLookupMixin, builtin_lookups.EndsWith
): ...
class KeyTransformIEndsWith(
    KeyTransformTextLookupMixin, builtin_lookups.IEndsWith
): ...
class KeyTransformRegex(KeyTransformTextLookupMixin, builtin_lookups.Regex): ...
class KeyTransformIRegex(
    KeyTransformTextLookupMixin, builtin_lookups.IRegex
): ...

class KeyTransformFactory:
    key_name: Any = ...
    def __init__(self, key_name: Any) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any): ...
