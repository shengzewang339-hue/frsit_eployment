#!/usr/bin/env python
"""
Test script to verify Django imports and setup
"""
import os
import sys
import django

# 添加当前目录到Python路径
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

print("Current working directory:", current_dir)
print("Python path:", sys.path)

# 设置Django配置
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'frsit_eployment_.settings')

try:
    # 初始化Django
    django.setup()
    print("Django setup successful!")
    
    # 测试导入Django组件
    from django.test import Client
    from django.conf import settings
    
    print("Django imports successful!")
    print("Installed apps:", settings.INSTALLED_APPS)
    
    # 测试创建客户端
    client = Client()
    print("Django test client created successfully!")
    
except Exception as e:
    print(f"Error during Django setup: {e}")
    import traceback
    traceback.print_exc()