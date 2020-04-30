from .models import Project
from lga.models import Lga
from mda.models import Ministry

import django_filters


class ProjectFilter(django_filters.FilterSet):
    phone = django_filters.CharFilter(lookup_expr='iexact')
    title = django_filters.CharFilter(lookup_expr='icontains')
    lga = django_filters.ModelChoiceFilter(
        queryset=Lga.objects.all())
    ministry = django_filters.ModelChoiceFilter(
        queryset=Ministry.objects.all())
    date = django_filters.CharFilter(lookup_expr='icontains')
    id = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Project
        fields = ['phone', 'title', 'lga', 'ministry', 'date']


class ProjectFilterSet(django_filters.FilterSet):
    created_min = django_filters.DateFilter(
        field_name='date', lookup_expr='gte')
    created_max = django_filters.DateFilter(
        field_name='date', lookup_expr='lte')

    class Meta:
        model = Project
        fields = ('date',)
