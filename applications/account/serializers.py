from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

from applications.bond.serializers import BondSerializer

UserModel = get_user_model()


class UserSerializer(ModelSerializer):
    bonds = BondSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email', 'bonds')
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create_user(
            **validated_data
        )
        return user
