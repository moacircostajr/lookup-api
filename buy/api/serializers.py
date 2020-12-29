from rest_framework.serializers import ModelSerializer

from buy.models import Buy


class BuySerializer(ModelSerializer):
    class Meta:
        model = Buy
        fields = '__all__'
