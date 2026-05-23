# FrameWord 后端

基于 Django + Django REST Framework 的后端基础框架。

## 技术栈

- Python 3.9+
- Django 4.2+
- Django REST Framework 3.14+
- Simple JWT
- django-cors-headers
- MySQL 8.0+ / mysqlclient

## 启动方法

```bash
# 1. 创建并激活虚拟环境
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 2. 安装依赖
pip install -r requirements.txt

# 3. 复制并修改环境变量
cp .env.example .env
# 编辑 .env 修改 SECRET_KEY 和 MySQL 密码

# 4. 在 MySQL 中创建数据库
mysql -u root -p -e "CREATE DATABASE frameword CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"

# 5. 执行数据库迁移
python manage.py migrate

# 6. 创建超级用户
python manage.py createsuperuser

# 7. 启动开发服务器
python manage.py runserver
```

服务器启动后访问 http://127.0.0.1:8000/

## 目录结构

```
backend/
  manage.py
  requirements.txt
  .env.example
  config/           # 项目配置
    settings/       # 分环境配置
      base.py       # 基础配置
      dev.py        # 开发环境
      prod.py       # 生产环境
    urls.py         # 路由入口
    asgi.py / wsgi.py
  apps/
    users/          # 用户模块
    common/         # 公共模块（响应格式、异常处理、分页等）
  logs/             # 日志目录
```

## 接口说明

| 方法 | 路径 | 说明 | 认证 |
|------|------|------|------|
| GET | /api/health/ | 健康检查 | 否 |
| POST | /api/users/register/ | 用户注册 | 否 |
| POST | /api/users/login/ | 用户登录 | 否 |
| POST | /api/users/token/refresh/ | 刷新 Token | 否 |
| GET | /api/users/me/ | 当前用户信息 | JWT |

## 新增应用步骤

1. 在 `apps/` 下创建新目录（如 `apps/dashboard/`）
2. 创建 `models.py`, `serializers.py`, `views.py`, `urls.py`
3. 在 `config/settings/base.py` 的 `INSTALLED_APPS` 中注册
4. 在 `config/urls.py` 中引入路由
5. 执行 `python manage.py makemigrations` 和 `python manage.py migrate`
