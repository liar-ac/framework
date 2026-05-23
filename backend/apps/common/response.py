"""
统一 API 响应格式
所有接口返回格式：
{
    "code": 200,
    "message": "success",
    "data": {}
}
"""
from rest_framework.response import Response


def success(data=None, message='success', code=200):
    """成功响应"""
    return Response({
        'code': code,
        'message': message,
        'data': data,
    }, status=code)


def error(message='error', code=400, data=None):
    """失败响应"""
    return Response({
        'code': code,
        'message': message,
        'data': data,
    }, status=code)
