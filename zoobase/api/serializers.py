from app.models import Stigmas
from rest_framework import serializers


class StigmasSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Stigmas
        fields = "__all__"