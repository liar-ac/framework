"""生产环境配置"""
from .base import *

DEBUG = False

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'yourdomain.com').split(',')
