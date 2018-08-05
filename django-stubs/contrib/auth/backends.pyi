from typing import Any, Optional, Set, Union

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AnonymousUser, User
from django.core.handlers.wsgi import WSGIRequest

UserModel: Any

class ModelBackend:
    def authenticate(
        self,
        request: Any,
        username: Optional[Union[str, int]] = ...,
        password: Optional[str] = ...,
        **kwargs: Any
    ) -> Optional[AbstractBaseUser]: ...
    def user_can_authenticate(
        self, user: Optional[AbstractBaseUser]
    ) -> bool: ...
    def get_user_permissions(
        self, user_obj: AbstractBaseUser, obj: None = ...
    ) -> Set[str]: ...
    def get_group_permissions(
        self, user_obj: AbstractBaseUser, obj: None = ...
    ) -> Set[str]: ...
    def get_all_permissions(
        self, user_obj: AbstractBaseUser, obj: Optional[str] = ...
    ) -> Set[str]: ...
    def has_perm(
        self,
        user_obj: Union[AnonymousUser, AbstractBaseUser],
        perm: str,
        obj: Optional[str] = ...,
    ) -> bool: ...
    def has_module_perms(
        self, user_obj: Union[AbstractBaseUser, AnonymousUser], app_label: str
    ) -> bool: ...
    def get_user(self, user_id: int) -> AbstractBaseUser: ...

class AllowAllUsersModelBackend(ModelBackend):
    def user_can_authenticate(self, user: AbstractBaseUser) -> bool: ...

class RemoteUserBackend(ModelBackend):
    create_unknown_user: bool = ...
    def authenticate(
        self, request: WSGIRequest, remote_user: Optional[str]
    ) -> Optional[User]: ...
    def clean_username(self, username: str) -> str: ...
    def configure_user(self, user: User) -> User: ...

class AllowAllUsersRemoteUserBackend(RemoteUserBackend):
    def user_can_authenticate(self, user: User) -> bool: ...
