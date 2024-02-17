import django_filters
from django_filters import DateFilter
from .models import *

class SubmissionFilter(django_filters.FilterSet):

    status = django_filters.ChoiceFilter(choices=Submission.get_status())
    date = django_filters.DateFilter(field_name='date_submitted', lookup_expr='exact')
    class Meta:
        model: Submission
        fields = '__all__'