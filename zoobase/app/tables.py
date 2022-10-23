import django_tables2 as tables
from django_tables2 import LazyPaginator, BooleanColumn

from .models import Stigmas


class StigmasTable(tables.Table):
    class Meta:
        model = Stigmas
        per_page = 5
        template_name = "app/table_style.html"
        exclude = ('slug', 'time_create', 'time_update')
        # attrs = {"class": 'table table-striped-columns'}]
        attrs = {"class": 'table table-light table-striped-columns'}


class HomeTable(StigmasTable):
    class Meta(StigmasTable.Meta):
        per_page = 10
        exclude = ('id', 'slug', 'time_create', 'time_update', 'author')


class SearchTable(StigmasTable):
    class Meta(StigmasTable.Meta):
        per_page = 5
