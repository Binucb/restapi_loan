from rest_framework import serializers

from loan_app import models

class ApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model =models.Approval
        fields = '__all__'