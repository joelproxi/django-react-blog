from rest_framework import serializers

from accounts.models import UserModel


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ('id',
                  'username',
                  'email',
                  'first_name',
                  'last_name',
                  'password',)
        extra_kwags = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = UserModel.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
