# FRSIT 部署项目 (简化测试版)

这是一个使用Django和Docker Compose部署的简化测试项目，专为快速验证而设计。

## 项目结构

```
frsit_eployment/
├── .github/
│   └── workflows/
│       └── test.yml          # GitHub Actions 工作流配置
├── frsit_eployment_/         # Django项目配置
├── practice/                 # Django应用
├── compose.yaml              # Docker Compose配置
├── Dockerfile                # Docker配置
├── requirements.txt          # Python依赖
└── manage.py                 # Django管理脚本
```

## 快速开始

1. 确保已安装Docker和Docker Compose
2. 克隆项目到本地
3. 在项目根目录运行以下命令启动服务：

```bash
docker-compose up --build
```

或者使用较新版本的Docker：

```bash
docker compose up --build
```

4. 访问应用：
   - 测试页面: http://localhost:8000/practice/hello/
   - Admin界面: http://localhost:8000/admin

## 停止服务

```bash
docker-compose down
```

## 本地开发

如果您想在本地运行而不用Docker：

1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. 运行开发服务器：
```bash
python manage.py runserver
```

3. 访问应用：
   - 测试页面: http://localhost:8000/practice/hello/
   - Admin界面: http://localhost:8000/admin

## 自动化测试

本项目包含GitHub Actions工作流配置，在代码推送到main/master分支或创建PR时自动运行测试：

- Python语法和依赖检查
- Django应用健康检查
- 简单的功能测试（访问hello视图）
- Docker Compose配置验证

## 特点

- 简化配置，仅包含最基本的Django功能
- 使用SQLite数据库，无需额外的数据库服务
- 不包含复杂的前端页面或静态文件
- 专为快速测试和验证设计
- 包含CI/CD工作流配置，支持自动化测试