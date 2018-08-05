from typing import Any, Optional

from django.db import models


class Redirect(models.Model):
    id: None
    site_id: int
    site: Any = ...
    old_path: str = ...
    new_path: str = ...
    class Meta:
        verbose_name: Any = ...
        verbose_name_plural: Any = ...
        db_table: str = ...
        unique_together: Any = ...
        ordering: Any = ...
