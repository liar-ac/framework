# Framework 前端

基于 Vue 3 + Vite 的前端基础框架。

## 技术栈

- Vue 3（Composition API）
- Vite 5
- Vue Router 4
- Pinia
- Axios

## 启动方法

```bash
# 安装依赖
npm install

# 启动开发服务器
npm run dev

# 打包生产环境
npm run build
```

开发服务器启动后访问 http://localhost:5173

## 目录结构

```
src/
  main.js          # 入口文件
  App.vue          # 根组件
  router/          # 路由配置
  stores/          # Pinia 状态管理
  api/             # API 请求封装
  views/           # 页面组件
  layout/          # 布局组件
  components/      # 公共组件
  utils/           # 工具函数
  styles/          # 全局样式
```

## 环境变量

- `.env.development` - 开发环境配置
- `.env.production` - 生产环境配置

| 变量 | 说明 |
|------|------|
| VITE_API_BASE_URL | 后端 API 基础地址 |

## 新增页面步骤

1. 在 `src/views/` 下创建新的 `.vue` 文件
2. 在 `src/router/index.js` 中添加路由
3. 如需调用后端接口，在 `src/api/` 下添加对应的 API 文件
