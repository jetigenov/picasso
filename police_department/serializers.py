from rest_framework import serializers

from police_department.models import Calls


class CallsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calls
        fields = '__all__'


