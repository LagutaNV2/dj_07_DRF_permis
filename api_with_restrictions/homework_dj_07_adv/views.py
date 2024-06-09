from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from rest_framework.response import Response
from django_filters import rest_framework as filters

from homework_dj_07_adv.filters import AdvertisementFilter
from homework_dj_07_adv.models import Advertisement
from homework_dj_07_adv.permissions import IsOwnerOrReadOnly #OwnerOrRead
from homework_dj_07_adv.serializers import AdvertisementSerializer

class AdvertisementViewSet(ModelViewSet):
    """
    ViewSet для объявлений.
    Валидация USERa объявления
    Фильтр объявления.
    
    """

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    # def get_permissions(self):
    #     """Получение прав для действий."""
    #     if self.action in ["create", "update", "partial_update"]:
    #         return [IsAuthenticated()]
    #     return []
    
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    
    filter_backends = [filters.DjangoFilterBackend]
    filter_fields = ['created_at', 'creator', 'status']
    # filter_class = AdvertisementFilter
    
    
    def get_permissions(self):
        """Получение прав для действий:
         Создавать - авторизованные пользователи;
         Просмотр -  авторизация не нужна;
         Обновлять -только его автор;
         Удаление – только его автор."""
        if self.action == 'create':
            return [IsAuthenticated()]
        else:
            return [IsOwnerOrReadOnly()]
    
    def list(self, request):
        list = Advertisement.objects.all()
        queryset = AdvertisementFilter(data=request.GET, queryset=list, request=request).qs
        serializer = AdvertisementSerializer(queryset, many=True)
        return Response(serializer.data)