from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

from applications.bond.serializers import BondSerializer


class UserSerializer(ModelSerializer):
    bonds = BondSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'bonds']