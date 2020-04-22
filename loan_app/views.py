from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets
from loan_app import serializers
from loan_app import models


# Create your views here.
class ApprovalViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ApprovalSerializer
    queryset = models.Approval.objects.all()


