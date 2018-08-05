from typing import Any, Optional, Type, Union

from django.db import models
from django.db.models.base import Model


class ContentTypeManager(models.Manager):
    creation_counter: int
    model: None
    name: None
    use_in_migrations: bool = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def get_by_natural_key(self, app_label: Any, model: Any): ...
    def get_for_model(
        self, model: Union[Type[Model], Model], for_concrete_model: bool = ...
    ) -> ContentType: ...
    def get_for_models(self, *models: Any, for_concrete_models: bool = ...): ...
    def get_for_id(self, id: int) -> ContentType: ...
    def clear_cache(self) -> None: ...

class ContentType(models.Model):
    id: int
    app_label: str = ...
    model: str = ...
    objects: Any = ...
    class Meta:
        verbose_name: Any = ...
        verbose_name_plural: Any = ...
        db_table: str = ...
        unique_together: Any = ...
    @property
    def name(self) -> str: ...
    def model_class(self) -> Type[Model]: ...
    def get_object_for_this_type(self, **kwargs: Any) -> Model: ...
    def get_all_objects_for_this_type(self, **kwargs: Any): ...
    def natural_key(self): ...
