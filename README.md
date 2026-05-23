# Framework

开箱即用的前后端分离基础开发框架，适用于管理系统、业务系统、个人项目的快速启动与二次开发。

---

## 技术栈

| 层级 | 技术 | 版本 |
|------|------|------|
| 前端框架 | Vue 3 (Composition API) | 3.4+ |
| 构建工具 | Vite | 5.4+ |
| 路由 | Vue Router | 4.3+ |
| 状态管理 | Pinia | 2.1+ |
| HTTP 客户端 | Axios | 1.7+ |
| 后端框架 | Django | 4.2+ |
| API 框架 | Django REST Framework | 3.14+ |
| 认证 | Simple JWT | 5.3+ |
| 数据库 | MySQL (PyMySQL 驱动) | 8.0+ |
| 跨域 | django-cors-headers | 4.3+ |

---

## 目录结构

```
Framework/
│
├── README.md                       ← 你正在看的文件
├── .gitignore
│
├── backend/                        ← 后端 Django 项目
│   ├── manage.py                   ← Django 命令行入口
│   ├── requirements.txt            ← Python 依赖清单
│   ├── .env.example                ← 环境变量模板（复制为 .env 使用）
│   ├── .gitignore
│   ├── README.md
│   │
│   ├── config/                     ← 项目配置目录
│   │   ├── __init__.py             ← PyMySQL 驱动初始化
│   │   ├── urls.py                 ← 顶层路由入口
│   │   ├── wsgi.py                 ← WSGI 入口（部署用）
│   │   ├── asgi.py                 ← ASGI 入口（异步部署用）
│   │   └── settings/
│   │       ├── __init__.py
│   │       ├── base.py             ← 所有环境共享的基础配置
│   │       ├── dev.py              ← 开发环境配置
│   │       └── prod.py             ← 生产环境配置
│   │
│   ├── apps/                       ← 业务应用目录
│   │   ├── common/                 ← 公共模块（所有应用复用）
│   │   │   ├── response.py         ← 统一 API 响应格式
│   │   │   ├── exceptions.py       ← 统一异常处理
│   │   │   ├── pagination.py       ← 统一分页配置
│   │   │   ├── permissions.py      ← 公共权限类
│   │   │   ├── views.py            ← 健康检查等公共视图
│   │   │   └── utils.py            ← 公共工具函数
│   │   │
│   │   └── users/                  ← 用户模块
│   │       ├── models.py           ← 自定义用户模型
│   │       ├── serializers.py      ← 注册/登录/信息序列化器
│   │       ├── views.py            ← 注册/登录/信息视图
│   │       ├── urls.py             ← 用户路由
│   │       ├── permissions.py      ← 用户相关权限
│   │       └── admin.py            ← 后台管理注册
│   │
│   ├── logs/                       ← 日志输出目录（自动生成）
│   ├── db.sqlite3                  ← SQLite 数据库文件（仅在切换回 SQLite 时生成）
│   └── venv/                       ← Python 虚拟环境（不提交）
│
└── frontend/                       ← 前端 Vue 3 项目
    ├── index.html                  ← HTML 入口
    ├── package.json                ← Node 依赖清单
    ├── vite.config.js              ← Vite 配置（含代理）
    ├── .env.development            ← 开发环境变量
    ├── .env.production             ← 生产环境变量
    ├── .gitignore
    ├── README.md
    │
    ├── public/                     ← 静态资源
    ├── node_modules/               ← 依赖（不提交）
    └── src/
        ├── main.js                 ← 应用入口
        ├── App.vue                 ← 根组件
        │
        ├── router/
        │   └── index.js            ← 路由配置 + 路由守卫
        │
        ├── stores/
        │   └── user.js             ← 用户状态（Pinia）
        │
        ├── api/
        │   ├── request.js          ← Axios 封装（拦截器/token/刷新）
        │   └── user.js             ← 用户相关 API
        │
        ├── views/
        │   ├── Login.vue           ← 登录页
        │   ├── Register.vue        ← 注册页
        │   ├── Home.vue            ← 首页（用户信息）
        │   ├── Dashboard.vue       ← 仪表盘（预留）
        │   ├── System.vue          ← 系统管理（预留）
        │   └── NotFound.vue        ← 404 页面
        │
        ├── layout/
        │   └── BasicLayout.vue     ← 后台主布局（侧边栏+顶部栏+内容区）
        │
        ├── components/
        │   ├── HeaderBar.vue       ← 顶部导航栏
        │   └── SideMenu.vue        ← 左侧菜单
        │
        ├── utils/
        │   └── auth.js             ← Token 存取工具
        │
        └── styles/
            └── main.css            ← 全局样式
```

---

## 环境要求

在开始之前，请确保本机已安装以下工具：

| 工具 | 最低版本 | 检查命令 |
|------|----------|----------|
| Python | 3.9+ | `python --version` |
| Node.js | 18+ | `node --version` |
| npm | 8+ | `npm --version` |
| MySQL | 8.0+ | `mysql --version` |
| Git | 任意 | `git --version` |

---

## 快速开始（完整步骤）

### 第一步：克隆项目

```bash
git clone https://github.com/liar-ac/frameword.git
cd frameword
```

### 第二步：准备 MySQL 数据库

确保 MySQL 服务已启动，然后创建数据库：

```bash
mysql -u root -p
```

```sql
CREATE DATABASE framework CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
EXIT;
```

### 第三步：启动后端

```bash
cd backend

# 创建 Python 虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# macOS / Linux:
source venv/bin/activate

# 安装 Python 依赖
pip install -r requirements.txt

# 复制环境变量文件并编辑
cp .env.example .env
```

编辑 `backend/.env`，至少修改以下两项：

```env
# 生成一个随机密钥替换掉默认值
SECRET_KEY=your-random-secret-key-here

# 填入你的 MySQL root 密码（如果有的话）
DB_PASSWORD=your-mysql-password
```

> 生成随机密钥的方法（在 Python 终端中执行）：
> ```python
> from django.core.management.utils import get_random_secret_key
> print(get_random_secret_key())
> ```

继续执行：

```bash
# 执行数据库迁移（自动创建表结构）
python manage.py migrate

# 创建管理员账号（按提示输入用户名、邮箱、密码）
python manage.py createsuperuser

# 启动后端开发服务器
python manage.py runserver
```

后端启动成功后会显示：

```
Starting development server at http://127.0.0.1:8000/
```

> 保持此终端运行，另开一个终端操作前端。

### 第四步：启动前端

```bash
cd frontend

# 安装 Node 依赖
npm install

# 启动前端开发服务器
npm run dev
```

前端启动成功后会显示：

```
Local: http://localhost:5173/
```

### 第五步：访问应用

浏览器打开 **http://localhost:5173/**

- 会自动跳转到登录页（因为未登录）
- 点击"去注册"注册新账号
- 注册成功后自动进入首页
- 首页会显示当前登录用户信息

---

## 环境变量说明

### 后端 `backend/.env`

| 变量 | 说明 | 默认值 | 必填 |
|------|------|--------|------|
| `DJANGO_SETTINGS_MODULE` | Django 配置模块 | `config.settings.dev` | 否 |
| `SECRET_KEY` | Django 加密密钥，生产环境必须更换 | 需自行设置 | **是** |
| `DEBUG` | 调试模式开关 | `True` | 否 |
| `DB_ENGINE` | 数据库引擎 | `django.db.backends.mysql` | 否 |
| `DB_NAME` | 数据库名称 | `framework` | 否 |
| `DB_USER` | 数据库用户名 | `root` | 否 |
| `DB_PASSWORD` | 数据库密码 | 空 | **是** |
| `DB_HOST` | 数据库地址 | `127.0.0.1` | 否 |
| `DB_PORT` | 数据库端口 | `3306` | 否 |
| `CORS_ALLOWED_ORIGINS` | 允许的前端跨域地址，逗号分隔 | `http://localhost:5173` | 否 |
| `JWT_ACCESS_TOKEN_LIFETIME_MINUTES` | Access Token 有效期（分钟） | `60` | 否 |
| `JWT_REFRESH_TOKEN_LIFETIME_DAYS` | Refresh Token 有效期（天） | `7` | 否 |

### 前端 `frontend/.env.development`

| 变量 | 说明 | 默认值 |
|------|------|--------|
| `VITE_API_BASE_URL` | 后端 API 基础地址 | `http://127.0.0.1:8000/api` |

### 前端 `frontend/.env.production`

| 变量 | 说明 | 默认值 |
|------|------|--------|
| `VITE_API_BASE_URL` | 生产环境 API 地址 | `/api` |

---

## 接口文档

所有接口统一返回格式：

```json
{
  "code": 200,
  "message": "操作说明",
  "data": { }
}
```

### 健康检查

```
GET /api/health/
无需认证

响应示例：
{
  "code": 200,
  "message": "服务运行正常",
  "data": { "status": "ok" }
}
```

### 用户注册

```
POST /api/users/register/
Content-Type: application/json
无需认证

请求体：
{
  "username": "testuser",
  "email": "test@example.com",
  "password": "yourpassword",
  "password2": "yourpassword"
}

成功响应（201）：
{
  "code": 201,
  "message": "注册成功",
  "data": {
    "user": {
      "id": 1,
      "username": "testuser",
      "email": "test@example.com",
      "nickname": "",
      "phone": "",
      "avatar": "",
      "is_staff": false,
      "date_joined": "2026-01-01T00:00:00+08:00"
    },
    "access": "eyJhbGciOiJIUzI1NiIs...",
    "refresh": "eyJhbGciOiJIUzI1NiIs..."
  }
}

字段说明：
- username：必填，3-150字符，不可重复
- email：选填，不可重复
- password：必填，至少6位
- password2：必填，必须与 password 一致
```

### 用户登录

```
POST /api/users/login/
Content-Type: application/json
无需认证

请求体：
{
  "username": "testuser",
  "password": "yourpassword"
}

成功响应（200）：
{
  "code": 200,
  "message": "登录成功",
  "data": {
    "user": { ... },
    "access": "eyJhbGciOiJIUzI1NiIs...",
    "refresh": "eyJhbGciOiJIUzI1NiIs..."
  }
}

错误响应（400）：
{
  "code": 400,
  "message": "用户名或密码错误",
  "data": null
}
```

### 刷新 Token

```
POST /api/users/token/refresh/
Content-Type: application/json
无需认证

请求体：
{
  "refresh": "eyJhbGciOiJIUzI1NiIs..."
}

成功响应（200）：
{
  "access": "eyJhbGciOiJIUzI1NiIs...",
  "refresh": "eyJhbGciOiJIUzI1NiIs..."
}

注意：此接口由前端 Axios 拦截器自动调用，一般无需手动使用。
Access Token 过期后，前端会自动用 Refresh Token 换取新 Token。
```

### 获取当前用户信息

```
GET /api/users/me/
Authorization: Bearer <access_token>
需要认证

成功响应（200）：
{
  "code": 200,
  "message": "success",
  "data": {
    "id": 1,
    "username": "testuser",
    "email": "test@example.com",
    "nickname": "",
    "phone": "",
    "avatar": "",
    "is_staff": false,
    "date_joined": "2026-01-01T00:00:00+08:00"
  }
}
```

---

## 认证机制说明

本框架使用 **JWT (JSON Web Token)** 认证，基于 `djangorestframework-simplejwt` 实现。

### 工作流程

```
1. 用户登录/注册 → 后端返回 access_token + refresh_token
2. 前端将两个 token 存入 localStorage
3. 每次请求时，Axios 请求拦截器自动在 Header 中携带：
   Authorization: Bearer <access_token>
4. access_token 过期（默认60分钟）后：
   → 前端 Axios 响应拦截器捕获 401 错误
   → 自动用 refresh_token 请求新的 access_token
   → 拿到新 token 后自动重试原请求
5. refresh_token 也过期（默认7天）后：
   → 清除本地 token，跳转登录页
```

---

## 前端架构说明

### Axios 请求封装 (`src/api/request.js`)

```
请求发出前 → 请求拦截器
  → 从 localStorage 读取 token
  → 自动添加 Authorization: Bearer <token>

响应返回后 → 响应拦截器
  → code 在 200-299 之间 → 正常返回 data
  → code 不在范围内 → 抛出业务错误
  → HTTP 401 → 尝试用 refresh_token 刷新
  → 刷新失败 → 清除 token，跳转登录页
```

### 路由守卫 (`src/router/index.js`)

```
访问任意路由前 → beforeEach 守卫
  → 目标页面需要登录 (requiresAuth) 且未登录 → 跳转 /login
  → 目标页面是登录/注册 (guest) 且已登录 → 跳转 /
  → 其他情况 → 正常放行
```

### 状态管理 (`src/stores/user.js`)

```
useUserStore
  ├── userInfo        当前用户信息对象
  ├── login(form)     调用登录 API → 存储 token → 保存用户信息
  ├── register(form)  调用注册 API → 存储 token → 保存用户信息
  ├── fetchUserInfo() 调用 /me 接口 → 更新 userInfo
  └── logout()        清除 userInfo → 清除 token
```

---

## 后端架构说明

### 统一响应格式 (`apps/common/response.py`)

```python
from apps.common.response import success, error

# 成功响应
return success(data={'key': 'value'}, message='操作成功')
# → {"code": 200, "message": "操作成功", "data": {"key": "value"}}

# 失败响应
return error(message='参数错误', code=400)
# → {"code": 400, "message": "参数错误", "data": null}
```

### 统一异常处理 (`apps/common/exceptions.py`)

所有 DRF 异常自动被捕获并转换为统一格式：

```
未登录访问 → {"code": 401, "message": "未登录或登录已过期", "data": null}
权限不足   → {"code": 403, "message": "没有权限执行此操作", "data": null}
字段错误   → {"code": 400, "message": "username: 该字段是必填项", "data": null}
```

### 分页配置 (`apps/common/pagination.py`)

```
GET /api/xxx/?page=2&page_size=20

默认每页 10 条，最大 100 条
可通过 query 参数 page 和 page_size 自定义
```

---

## 后续开发指南

### 新增后端模块（示例：添加文章模块）

```bash
cd backend/apps
mkdir articles
```

创建 `apps/articles/models.py`：

```python
from django.db import models

class Article(models.Model):
    title = models.CharField('标题', max_length=200)
    content = models.TextField('内容')
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='作者')
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'articles'
        verbose_name = '文章'
        ordering = ['-created_at']
```

创建 `apps/articles/serializers.py`、`views.py`、`urls.py`，可参考 `apps/users/` 的写法。

注册应用：在 `config/settings/base.py` 的 `INSTALLED_APPS` 中添加 `'apps.articles'`。

引入路由：在 `config/urls.py` 中添加：

```python
path('api/articles/', include('apps.articles.urls')),
```

执行迁移：

```bash
python manage.py makemigrations articles
python manage.py migrate
```

### 新增前端页面（示例：添加文章列表页）

1. 创建 `frontend/src/views/ArticleList.vue`
2. 在 `frontend/src/api/` 下创建 `article.js` 封装接口
3. 在 `frontend/src/router/index.js` 中添加路由：

```javascript
{
  path: 'articles',
  name: 'ArticleList',
  component: () => import('../views/ArticleList.vue'),
}
```

4. 在 `frontend/src/components/SideMenu.vue` 中添加菜单项

---

## 预留模块

框架已预留以下管理后台常见模块的页面入口，仅含示例页面，无业务逻辑：

| 模块 | 前端路由 | 前端文件 | 后端应用（待创建） |
|------|----------|----------|---------------------|
| 仪表盘 | `/dashboard` | `views/Dashboard.vue` | `apps/dashboard/` |
| 系统管理 | `/system` | `views/System.vue` | `apps/system/` |
| 角色管理 | - | 待创建 | `apps/role/` |
| 权限管理 | - | 待创建 | `apps/permission/` |
| 菜单管理 | - | 待创建 | `apps/menu/` |

---

## 生产环境部署要点

### 后端

```bash
# 编辑 .env
DEBUG=False
SECRET_KEY=使用随机生成的强密钥
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DJANGO_SETTINGS_MODULE=config.settings.prod

# 收集静态文件
python manage.py collectstatic

# 使用 Gunicorn 启动（需额外安装）
pip install gunicorn
gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 4
```

### 前端

```bash
# 构建生产版本
npm run build

# 产物在 dist/ 目录，用 Nginx 部署
```

Nginx 参考配置：

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    # 前端静态文件
    location / {
        root /path/to/frontend/dist;
        try_files $uri $uri/ /index.html;
    }

    # 后端 API 代理
    location /api/ {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

---

## 常见问题排查

### 后端相关

**Q: `pip install` 报错找不到 mysql_config**
A: Windows 上安装 `mysqlclient` 需要 C 编译器。本框架已使用 `PyMySQL`（纯 Python 驱动）替代，直接 `pip install -r requirements.txt` 即可。

**Q: 启动报错 `ImproperlyConfigured: ... 'mysql' isn't an available database backend`**
A: 确保已安装 PyMySQL：`pip install PyMySQL`

**Q: 启动报错 `django.db.utils.OperationalError: (2003, "Can't connect to MySQL server")`**
A: 检查 MySQL 服务是否启动，以及 `.env` 中 `DB_HOST`、`DB_PORT`、`DB_USER`、`DB_PASSWORD` 是否正确。

**Q: 启动报错 `Unknown database 'framework'`**
A: 需要先在 MySQL 中创建数据库：
```sql
CREATE DATABASE framework CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

**Q: 迁移报错 `InconsistentMigrationHistory`**
A: 删除数据库重新创建，再执行 `python manage.py migrate`。

**Q: 如何切换回 SQLite 进行本地开发？**
A: 编辑 `.env`：
```env
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
```
同时将 `config/__init__.py` 中的 `pymysql.install_as_MySQLdb()` 注释掉。

### 前端相关

**Q: `npm install` 很慢**
A: 使用国内镜像：`npm config set registry https://registry.npmmirror.com`

**Q: 页面请求后端报 CORS 错误**
A: 检查后端 `.env` 中 `CORS_ALLOWED_ORIGINS` 是否包含 `http://localhost:5173`，修改后需重启后端。

**Q: 登录成功但刷新页面后跳回登录页**
A: 打开浏览器开发者工具 → Application → Local Storage，检查是否存在 `access_token`。如果不存在，检查 Axios 响应是否正确返回了 `data.access`。

**Q: 接口返回 401 但 token 还在**
A: Access Token 已过期，检查 Refresh Token 是否有效。可在浏览器控制台查看是否有 `/token/refresh/` 的请求。如果 Refresh Token 也过期了，需要重新登录。

**Q: Vite 代理不生效，请求直接发到 localhost:5173**
A: 确保 `vite.config.js` 中的 proxy 配置正确，且前端代码中 `VITE_API_BASE_URL` 在开发环境下不要包含完整域名（或直接留空让代理接管）。当前配置使用 `/api` 前缀即可。

---

## 命令速查表

```bash
# ===== 后端 =====
python manage.py runserver              # 启动开发服务器
python manage.py migrate                # 执行数据库迁移
python manage.py makemigrations <app>   # 生成迁移文件
python manage.py createsuperuser        # 创建管理员
python manage.py shell                  # 进入 Django Shell
python manage.py collectstatic          # 收集静态文件（生产环境）

# ===== 前端 =====
npm run dev                             # 启动开发服务器
npm run build                           # 构建生产版本
npm run preview                         # 预览生产构建
```

---

## License

MIT
