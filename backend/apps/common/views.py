"""
公共视图
"""
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from apps.common.response import success


@api_view(['GET'])
@permission_classes([AllowAny])
def health_check(request):
    """健康检查接口，用于运维监控和负载均衡探活"""
    return success(data={'status': 'ok'}, message='服务运行正常')
