"""
用户视图
"""
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from apps.common.response import success, error
from .models import User
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserInfoSerializer


class RegisterView(generics.CreateAPIView):
    """用户注册"""
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # 注册成功后直接生成 JWT token
        refresh = RefreshToken.for_user(user)
        return success(data={
            'user': UserInfoSerializer(user).data,
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }, message='注册成功', code=201)


class LoginView(generics.GenericAPIView):
    """用户登录"""
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        return success(data={
            'user': UserInfoSerializer(user).data,
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }, message='登录成功')


class UserInfoView(generics.RetrieveAPIView):
    """获取当前登录用户信息"""
    serializer_class = UserInfoSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def retrieve(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user)
        return success(data=serializer.data)
