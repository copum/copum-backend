from rest_framework import serializers

from .models import User, Profile


class UserSerializer(serializers.ModelSerializer) :
    class Meta :
        model = User
        fields = ('user_id', 'email', 'nickname', 'password', 'login_type')

class ProfileSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Profile
        fields = ('user')
