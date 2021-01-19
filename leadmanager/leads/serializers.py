from rest_framework import serializers
from .models import Lead

# Serializers define the API representation.
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'