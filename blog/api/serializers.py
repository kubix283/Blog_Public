from rest_framework import serializers
from accounts.models import CustomUser
from blog_app.models import Post, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'age',
                  'about_me', 'phone', 'sex']
        


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'age',
                  'about_me', 'phone', 'sex']