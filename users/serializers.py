from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ["pk", "email", "user_id", "profile_image"]

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(
            email = validated_data['email'],
            user_id = validated_data['user_id'],
            profile_image = validated_data['profile_image']
        )
        return user
    
class UserDetailSerializer(serializers.ModelSerializer) :
    class Meta :
        model = User
        fields = "__all__"  