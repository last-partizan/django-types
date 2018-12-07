from typing import Any, Dict, Optional, Type, Union

from django.core.handlers.wsgi import WSGIRequest
from django.db.models.base import Model
from django.forms.forms import BaseForm, Form
from django.forms.models import ModelForm
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.utils.datastructures import MultiValueDict
from django.views.generic.base import ContextMixin, TemplateResponseMixin, View
from django.views.generic.detail import BaseDetailView, SingleObjectMixin, SingleObjectTemplateResponseMixin

class FormMixin(ContextMixin):
    initial: Any = ...
    form_class: Any = ...
    success_url: Any = ...
    prefix: Any = ...
    def get_initial(self) -> Dict[Any, Any]: ...
    def get_prefix(self) -> None: ...
    def get_form_class(self) -> Type[Form]: ...
    def get_form(self, form_class: None = ...) -> BaseForm: ...
    def get_form_kwargs(self) -> Dict[str, Optional[Union[Dict[str, str], MultiValueDict]]]: ...
    def get_success_url(self) -> str: ...
    def form_valid(self, form: BaseForm) -> HttpResponseRedirect: ...
    def form_invalid(self, form: Form) -> TemplateResponse: ...
    def get_context_data(self, **kwargs: Any) -> Dict[str, Union[Model, BaseForm, TemplateResponseMixin]]: ...

class ModelFormMixin(FormMixin, SingleObjectMixin):
    request: django.core.handlers.wsgi.WSGIRequest
    fields: Any = ...
    def get_form_class(self) -> Type[ModelForm]: ...
    def get_form_kwargs(self) -> Dict[str, Optional[Union[Dict[Any, Any], Model, MultiValueDict]]]: ...
    def get_success_url(self) -> str: ...
    object: Any = ...
    def form_valid(self, form: ModelForm) -> HttpResponseRedirect: ...

class ProcessFormView(View):
    def get(self, request: WSGIRequest, *args: Any, **kwargs: Any) -> TemplateResponse: ...
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse: ...
    def put(self, *args: Any, **kwargs: Any): ...

class BaseFormView(FormMixin, ProcessFormView): ...
class FormView(TemplateResponseMixin, BaseFormView): ...

class BaseCreateView(ModelFormMixin, ProcessFormView):
    object: Any = ...
    def get(self, request: WSGIRequest, *args: Any, **kwargs: Any) -> TemplateResponse: ...
    def post(self, request: WSGIRequest, *args: Any, **kwargs: Any) -> HttpResponse: ...

class CreateView(SingleObjectTemplateResponseMixin, BaseCreateView):
    template_name_suffix: str = ...

class BaseUpdateView(ModelFormMixin, ProcessFormView):
    object: Any = ...
    def get(self, request: WSGIRequest, *args: Any, **kwargs: Any) -> TemplateResponse: ...
    def post(self, request: WSGIRequest, *args: Any, **kwargs: Any) -> HttpResponse: ...

class UpdateView(SingleObjectTemplateResponseMixin, BaseUpdateView):
    template_name_suffix: str = ...

class DeletionMixin:
    success_url: Any = ...
    object: Any = ...
    def delete(self, request: WSGIRequest, *args: Any, **kwargs: Any) -> HttpResponseRedirect: ...
    def post(self, request: WSGIRequest, *args: Any, **kwargs: Any) -> HttpResponseRedirect: ...
    def get_success_url(self) -> str: ...

class BaseDeleteView(DeletionMixin, BaseDetailView): ...

class DeleteView(SingleObjectTemplateResponseMixin, BaseDeleteView):
    template_name_suffix: str = ...