from rest_framework.serializers import ModelSerializer

from cash.models import Cash


class CashSerializer(ModelSerializer):
    class Meta:
        model = Cash
        fields = '__all__'
