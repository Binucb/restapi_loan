from rest_framework import serializers

from loan_app import models

class UserProfileSerializer(serializers.ModelSerializer):
    class.Meta:
        model =models.Approval
        fields = '__all__'