"""
公共权限类
"""
from rest_framework.permissions import BasePermission


class IsAdminUser(BasePermission):
    """仅管理员可访问"""
    def has_permission(self, request, view):
        return request.user and request.user.is_staff


class IsOwnerOrReadOnly(BasePermission):
    """对象所有者可写，其他人只读"""
    def has_object_permission(self, request, view, obj):
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        return obj == request.user
