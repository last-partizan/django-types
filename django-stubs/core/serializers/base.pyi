from collections import OrderedDict
from io import BufferedReader, StringIO, TextIOWrapper
from typing import Any, Dict, Iterator, List, Optional, Tuple, Type, Union
from uuid import UUID

from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.core.management.base import OutputWrapper
from django.core.serializers.xml_serializer import Deserializer
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.db.models.query import QuerySet


class SerializerDoesNotExist(KeyError): ...
class SerializationError(Exception): ...

class DeserializationError(Exception):
    @classmethod
    def WithData(
        cls,
        original_exc: Union[ValidationError, ObjectDoesNotExist],
        model: str,
        fk: Union[str, int],
        field_value: Optional[Union[str, List[str]]],
    ) -> DeserializationError: ...

class M2MDeserializationError(Exception):
    original_exc: django.core.exceptions.ObjectDoesNotExist = ...
    pk: List[str] = ...
    def __init__(
        self,
        original_exc: Union[ValidationError, ObjectDoesNotExist],
        pk: Union[str, List[str]],
    ) -> None: ...

class ProgressBar:
    progress_width: int = ...
    output: None = ...
    total_count: int = ...
    prev_done: int = ...
    def __init__(
        self, output: Optional[Union[StringIO, OutputWrapper]], total_count: int
    ) -> None: ...
    def update(self, count: int) -> None: ...

class Serializer:
    internal_use_only: bool = ...
    progress_class: Any = ...
    stream_class: Any = ...
    options: Any = ...
    stream: Any = ...
    selected_fields: Any = ...
    use_natural_foreign_keys: Any = ...
    use_natural_primary_keys: Any = ...
    first: bool = ...
    def serialize(
        self,
        queryset: Union[QuerySet, List[Model], Iterator[Any]],
        *,
        stream: Optional[Any] = ...,
        fields: Optional[Any] = ...,
        use_natural_foreign_keys: bool = ...,
        use_natural_primary_keys: bool = ...,
        progress_output: Optional[Any] = ...,
        object_count: int = ...,
        **options: Any
    ) -> Optional[Union[str, bytes, List[OrderedDict]]]: ...
    def start_serialization(self) -> None: ...
    def end_serialization(self) -> None: ...
    def start_object(self, obj: Any) -> None: ...
    def end_object(self, obj: Any) -> None: ...
    def handle_field(self, obj: Any, field: Any) -> None: ...
    def handle_fk_field(self, obj: Any, field: Any) -> None: ...
    def handle_m2m_field(self, obj: Any, field: Any) -> None: ...
    def getvalue(self) -> Optional[Union[str, bytes]]: ...

class Deserializer:
    options: Any = ...
    stream: Any = ...
    def __init__(
        self,
        stream_or_string: Union[str, TextIOWrapper, BufferedReader],
        **options: Any
    ) -> None: ...
    def __iter__(self) -> Deserializer: ...
    def __next__(self) -> None: ...

class DeserializedObject:
    object: django.db.models.base.Model = ...
    m2m_data: Dict[Any, Any] = ...
    def __init__(
        self, obj: Model, m2m_data: Optional[Dict[str, List[int]]] = ...
    ) -> None: ...
    def save(
        self, save_m2m: bool = ..., using: Optional[str] = ..., **kwargs: Any
    ) -> None: ...

def build_instance(
    Model: Type[Model], data: Dict[str, Any], db: str
) -> Model: ...
def deserialize_m2m_values(
    field: ManyToManyField,
    field_value: Union[List[List[str]], List[Union[int, str]]],
    using: str,
) -> List[int]: ...
def deserialize_fk_value(
    field: ForeignKey,
    field_value: Optional[Union[int, Tuple[str], str, List[str]]],
    using: str,
) -> Optional[Union[str, UUID, int]]: ...
