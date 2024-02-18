import django_filters
from django_filters import DateFilter
from .models import *

class SubmissionFilter(django_filters.FilterSet):

    status = django_filters.ChoiceFilter(choices=Snippet.get_status())
    date = django_filters.DateFilter(field_name='created_at', lookup_expr='exact')
    class Meta:
        model: Snippet
        fields = '__all__'