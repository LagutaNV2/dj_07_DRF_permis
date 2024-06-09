from django_filters import rest_framework as filters

from homework_dj_07_adv.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """
      Фильтры для объявлений:
      - по дате (используйте DateFromToRangeFilter...)
      - по статусу
    """

    # TODO: задайте требуемые фильтры
    created_at = filters.DateFromToRangeFilter()
    is_active = filters.BooleanFilter(lookup_expr='exact')  # boolean
    creator = filters.NumberFilter(lookup_expr='id__exact')  # FK
    
    class Meta:
        model = Advertisement
        fields = ['created_at', 'creator', 'status']
       

    
