"""
统一异常处理
捕获 DRF 异常并返回统一格式响应
"""
from rest_framework.views import exception_handler
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated, PermissionDenied


def custom_exception_handler(exc, context):
    """自定义异常处理器，将 DRF 异常包装为统一响应格式"""
    response = exception_handler(exc, context)

    if response is not None:
        # 默认使用异常自带的状态码
        code = response.status_code
        message = '请求失败'

        if isinstance(exc, NotAuthenticated):
            message = '未登录或登录已过期'
            code = 401
        elif isinstance(exc, AuthenticationFailed):
            message = '认证失败'
            code = 401
        elif isinstance(exc, PermissionDenied):
            message = '没有权限执行此操作'
            code = 403
        elif hasattr(exc, 'detail'):
            if isinstance(exc.detail, dict):
                # 字段验证错误，拼接所有错误信息
                messages = []
                for field, errors in exc.detail.items():
                    for error in errors:
                        messages.append(f'{field}: {error}')
                message = '; '.join(messages)
            elif isinstance(exc.detail, list):
                message = '; '.join(str(e) for e in exc.detail)
            else:
                message = str(exc.detail)

        response.data = {
            'code': code,
            'message': message,
            'data': None,
        }

    return response
