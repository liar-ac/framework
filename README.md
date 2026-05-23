# FrameWord - 全栈基础开发框架

前后端分离的基础开发框架，可直接复制用于各类管理系统、业务系统、个人项目的二次开发。

## 技术栈

| 层级 | 技术 |
|------|------|
| 前端 | Vue 3 + Vite + Vue Router + Pinia + Axios |
| 后端 | Django 4.2 + Django REST Framework + Simple JWT |
| 数据库 | MySQL 8.0+ |

## 目录结构

```
frameword/
├── backend/                # 后端 Django 项目
│   ├── manage.py
│   ├── requirements.txt
│   ├── .env.example
│   ├── config/             # 项目配置
│   │   ├── settings/
│   │   │   ├── base.py     # 基础配置
│   │   │   ├── dev.py      # 开发环境
│   │   │   └── prod.py     # 生产环境
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   ├── apps/
│   │   ├── users/          # 用户模块（注册/登录/信息）
│   │   └── common/         # 公共模块（响应/异常/分页/权限）
│   └── logs/
├── frontend/               # 前端 Vue 3 项目
│   ├── package.json
│   ├── vite.config.js
│   ├── .env.development
│   ├── .env.production
│   ├── index.html
│   └── src/
│       ├── main.js
│       ├── App.vue
│       ├── router/         # 路由配置
│       ├── stores/         # Pinia 状态管理
│       ├── api/            # API 请求封装
│       ├── views/          # 页面组件
│       ├── layout/         # 布局组件
│       ├── components/     # 公共组件
│       ├── utils/          # 工具函数
│       └── styles/         # 全局样式
└── README.md
```

## 后端启动

```bash
cd backend

# 创建虚拟环境
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate    # macOS/Linux

# 安装依赖
pip install -r requirements.txt

# 复制环境变量
cp .env.example .env
# 编辑 .env 修改 SECRET_KEY 和 MySQL 密码

# 在 MySQL 中创建数据库
mysql -u root -p -e "CREATE DATABASE frameword CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"

# 数据库迁移
python manage.py migrate

# 创建超级用户
python manage.py createsuperuser

# 启动
python manage.py runserver
```

后端运行在 http://127.0.0.1:8000/

## 前端启动

```bash
cd frontend

# 安装依赖
npm install

# 启动开发服务器
npm run dev
```

前端运行在 http://localhost:5173/

## 环境变量说明

### 后端 (.env)

| 变量 | 说明 | 默认值 |
|------|------|--------|
| SECRET_KEY | Django 密钥 | 需自行设置 |
| DEBUG | 调试模式 | True |
| DB_ENGINE | 数据库引擎 | django.db.backends.mysql |
| DB_NAME | 数据库名 | frameword |
| DB_USER | 数据库用户 | root |
| DB_PASSWORD | 数据库密码 | - |
| DB_HOST | 数据库地址 | 127.0.0.1 |
| DB_PORT | 数据库端口 | 3306 |
| CORS_ALLOWED_ORIGINS | 允许的跨域来源 | http://localhost:5173 |
| JWT_ACCESS_TOKEN_LIFETIME_MINUTES | Access Token 有效期(分钟) | 60 |
| JWT_REFRESH_TOKEN_LIFETIME_DAYS | Refresh Token 有效期(天) | 7 |

### 前端 (.env.development / .env.production)

| 变量 | 说明 | 默认值 |
|------|------|--------|
| VITE_API_BASE_URL | 后端 API 地址 | http://127.0.0.1:8000/api |

## 接口说明

| 方法 | 路径 | 说明 | 认证 |
|------|------|------|------|
| GET | /api/health/ | 健康检查 | 否 |
| POST | /api/users/register/ | 用户注册 | 否 |
| POST | /api/users/login/ | 用户登录 | 否 |
| POST | /api/users/token/refresh/ | 刷新 Token | 否 |
| GET | /api/users/me/ | 获取当前用户信息 | JWT |

### 注册接口

```
POST /api/users/register/
{
  "username": "testuser",
  "email": "test@example.com",
  "password": "123456",
  "password2": "123456"
}
```

### 登录接口

```
POST /api/users/login/
{
  "username": "testuser",
  "password": "123456"
}
```

### 响应格式

```json
{
  "code": 200,
  "message": "success",
  "data": {
    "user": { "id": 1, "username": "testuser", ... },
    "access": "eyJ...",
    "refresh": "eyJ..."
  }
}
```

## 后续开发建议

### 新增后端模块

1. 在 `backend/apps/` 下创建新应用目录
2. 编写 `models.py` → `serializers.py` → `views.py` → `urls.py`
3. 在 `config/settings/base.py` 的 `INSTALLED_APPS` 中注册
4. 在 `config/urls.py` 中引入新应用路由
5. 执行 `python manage.py makemigrations && python manage.py migrate`

### 新增前端页面

1. 在 `frontend/src/views/` 下创建新页面组件
2. 在 `frontend/src/router/index.js` 中添加路由
3. 如需调用后端接口，在 `frontend/src/api/` 下添加 API 文件
4. 如需全局状态，在 `frontend/src/stores/` 下创建 Pinia store

### 预留模块结构

框架已预留以下管理后台常见模块的页面入口（仅含示例页面，无业务逻辑）：

- `Dashboard` - 仪表盘 (/dashboard)
- `System` - 系统管理 (/system)

后续可在 `backend/apps/` 下创建对应的 `dashboard`、`system`、`role`、`permission`、`menu` 等应用。

## 测试步骤

### 测试注册

```bash
curl -X POST http://127.0.0.1:8000/api/users/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"test","password":"123456","password2":"123456"}'
```

### 测试登录

```bash
curl -X POST http://127.0.0.1:8000/api/users/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"test","password":"123456"}'
```

### 测试获取用户信息

```bash
# 将 <token> 替换为登录返回的 access token
curl http://127.0.0.1:8000/api/users/me/ \
  -H "Authorization: Bearer <token>"
```

### 测试健康检查

```bash
curl http://127.0.0.1:8000/api/health/
```

## 常见问题

**Q: 后端启动报错 `ModuleNotFoundError: No module named 'dotenv'`**
A: 确保已安装依赖 `pip install -r requirements.txt`

**Q: 前端请求后端报 CORS 错误**
A: 检查后端 `.env` 中 `CORS_ALLOWED_ORIGINS` 是否包含前端地址

**Q: 登录后刷新页面需要重新登录**
A: 检查 Token 是否正确存储在 localStorage，以及后端 JWT 配置是否正确

**Q: 切换数据库后报错**
A: 修改 `.env` 中的 `DB_ENGINE` 等配置后，需要重新执行 `python manage.py migrate`

**Q: 安装 mysqlclient 报错**
A: Windows 上需要先安装 MySQL C Connector。可从 https://dev.mysql.com/downloads/connector/c/ 下载安装，或改用 `pip install pymysql` 并在 `config/__init__.py` 中添加：
```python
import pymysql
pymysql.install_as_MySQLdb()
```
