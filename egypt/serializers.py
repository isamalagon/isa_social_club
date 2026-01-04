from rest_framework import serializers
from .models import EgyptTip

class EgyptTipSerializer(serializers.ModelSerializer):
    class Meta:
        model = EgyptTip
        fields = '__all__'
