from rest_framework import serializers
from api.models import FundoImobiliario


class FundoImobiliarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = FundoImobiliario
        fields = '__all__'
