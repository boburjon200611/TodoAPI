from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, ListCreateAPIView
from Todoapp.models import Plan
from Todoapp.Serializer import PlanSerializer,CreateSerializer
from rest_framework.permissions import IsAuthenticated


class PlanListAPIView(ListCreateAPIView):
    serializer_class = PlanSerializer
    # authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    def get_queryset(self):
        plans = Plan.objects.filter(user=self.request.user)
        return plans

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

# class PlanCreateAPIView(CreateAPIView):
#     queryset = Plan.objects.all()
#     serializer_class = PlanSerializer

class RetriveAPIView(RetrieveAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

