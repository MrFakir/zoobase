from django.core.exceptions import ValidationError
from django_tables2 import LazyPaginator

from .models import Stigmas
from .tables import StigmasTable


class TableViewsMixin:
    model = Stigmas
    paginator_class = LazyPaginator
