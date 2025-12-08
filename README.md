# FRSIT 部署项目

这是一个使用Django和Docker Compose部署的项目。

## 项目结构

```
frsit_eployment/
├── frsit_eployment_/     # Django项目配置
├── practice/             # Django应用
├── compose.yaml          # Docker Compose配置
├── Dockerfile            # Docker配置
├── requirements.txt      # Python依赖
└── manage.py             # Django管理脚本
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
   - Django应用: http://localhost:8000
   - Admin界面: http://localhost:8000/admin

## 停止服务

```bash
docker-compose down
```

## 数据库

项目使用PostgreSQL数据库，默认配置为：
- 数据库名: frsit_db
- 用户名: frsit_user
- 密码: frsit_password
- 端口: 5432

## 环境变量

可以通过环境变量覆盖默认的数据库配置：
- POSTGRES_DB
- POSTGRES_USER
- POSTGRES_PASSWORD
- DB_HOST
- DB_PORT