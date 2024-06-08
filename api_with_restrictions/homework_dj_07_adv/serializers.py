from django.contrib.auth.models import User
from rest_framework import serializers

from homework_dj_07_adv.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(read_only=True,)

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        """Метод для создания Advertisement"""

        # Простановка значения поля "создатель" по-умолчанию:
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        print(f'create advertise: {self.context=}, {validated_data=}')
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""

        # TODO: добавьте требуемую валидацию
        # у пользователя не больше 10 открытых объявлений
        # self.initial_data.get('status')
        
        counts = Advertisement.objects.filter(status="OPEN", creator=self.context["request"].user).count()
        status = data.get("status")
        method_request = self.context["request"].method
        
        print(f'validate advertise: {self.context=}, {data=}, {method_request=}, {counts=}')
        if counts >= 10 and method_request == "POST" or status == "OPEN":
            raise serializers.ValidationError("Превышен лимит для открытых объявлений (>10)")

        return data
