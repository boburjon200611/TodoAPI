from rest_framework.serializers import ModelSerializer
from .models import Plan

class PlanSerializer(ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'

class CreateSerializer(ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'