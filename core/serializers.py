from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer

from core.models import User


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer):
        model = User
        fields = ['id','first_name','last_name','email','username']

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer):
        model = User
        fields = ['id','first_name','last_name','email','username','password']
