"""
统一分页配置
"""
from rest_framework.pagination import PageNumberPagination


class StandardPagination(PageNumberPagination):
    """标准分页器，支持通过 query 参数自定义每页数量"""
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
