from rest_framework import serializers
 
from .models import QuesModel


class QuesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model= QuesModel
        fields = "__all__" 