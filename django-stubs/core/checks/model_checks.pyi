from typing import Any, List, Optional

from django.core.checks.messages import Warning


def check_all_models(
    app_configs: None = ..., **kwargs: Any
) -> List[Warning]: ...
def check_lazy_references(
    app_configs: None = ..., **kwargs: Any
) -> List[Any]: ...
