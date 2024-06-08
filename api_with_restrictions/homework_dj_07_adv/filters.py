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
    
    class Meta:
        model = Advertisement
        fields = ['created_at', 'creator', 'status']
       

    
