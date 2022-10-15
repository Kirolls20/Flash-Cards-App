import django_filters
from django_filters import CharFilter
from .models import *

class CardFilter(django_filters.FilterSet):
   front =CharFilter(field_name='frontcard',lookup_expr='istartswith')
   back = CharFilter(field_name='backcard',lookup_expr='icontains')
   class Meta:
      model= Card
      fields=['card_type']
      
      


