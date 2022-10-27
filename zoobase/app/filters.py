import django_filters
from django_filters.widgets import LinkWidget

from django.db import models
from .models import Stigmas, TypeStigmas


class StigmasFilter(django_filters.FilterSet):
    number__gt = django_filters.NumberFilter(field_name='number', lookup_expr='gte', )
    number__lt = django_filters.NumberFilter(field_name='number', lookup_expr='lte', )
    phone_number = django_filters.NumberFilter(field_name='phone_number',
                                               help_text='Введите номер телефона без восьмёрки')
    date_created = django_filters.DateFilter(field_name='date_created')
    date_created__gt = django_filters.DateFilter(field_name='date_created', lookup_expr='gte')
    date_created__lt = django_filters.DateFilter(field_name='date_created', lookup_expr='lte')

    class Meta:
        model = Stigmas
        fields = ['number', 'number__gt', 'number__lt', 'tag_number', 'type_animal', 'sex', 'the_pet', 'master',
                  'type_id', 'phone_number', 'date_created',
                  'description', 'author']
        filter_overrides = {
            models.CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            },
        }
