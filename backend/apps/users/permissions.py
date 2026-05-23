"""
用户模块权限类
"""
from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """仅对象所有者可访问"""
    def has_object_permission(self, request, view, obj):
        return obj == request.user
