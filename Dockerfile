# 使用官方Python运行时作为基础镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 设置环境变量
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 安装系统依赖
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
        postgresql-dev \
        gcc \
        python3-dev \
        musl-dev \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 升级pip
RUN pip install --upgrade pip

# 复制requirements.txt（如果存在）
COPY requirements.txt /app/requirements.txt

# 安装Python依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目文件
COPY . /app/

# 暴露端口
EXPOSE 8000

# 收集静态文件
RUN python manage.py collectstatic --noinput

# 启动命令
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "frsit_eployment_.wsgi:application"]