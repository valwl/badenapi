from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from . models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .custom_auth import CustomAuth

#we need add validation
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'login'
    login = serializers.CharField(max_length=255)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        login = attrs.get('login')
        password = attrs.get('password')
        if login and password:
            user = self.user_authenticate(login, password)
            if user:
                data = {}
                refresh = self.get_token(user)
                data['refresh'] = str(refresh)
                data['access'] = str(refresh.access_token)
                return data
            else:
                raise serializers.ValidationError('user not found')
        else:
            raise serializers.ValidationError('password or login no requared')

    def user_authenticate(self, login, password):
        user = CustomAuth().authenticate(request=None, login=login, password=password)
        return user


class CustomUserSerializer(serializers.ModelSerializer):
    login = serializers.CharField(max_length=255)
    class Meta:
        model = CustomUser
        fields = '__all__'


# class CustomUserLoginSerializer(serializers.Serializer):
#     login = serializers.CharField()
#     password = serializers.CharField(write_only=True)
#
#     def validate(self, data):
#         login = data.get('login', None)
#         password = data.get('password', None)
#         if '@' in login:
#             user = CustomUser.objects.get(email=login)
#         else:
#             user = CustomUser.objects.get(phone_number=login)
#         if user is None:
#             raise serializers.ValidationError('this user is none')
#         if not user.check_password(password):
#             raise serializers.ValidationError('password is not correct')
#         return data







