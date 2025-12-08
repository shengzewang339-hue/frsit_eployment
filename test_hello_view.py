#!/usr/bin/env python
"""
Test script for the hello view
"""
import os
import sys
import django
from django.conf import settings
from django.test import Client
from django.test.utils import setup_test_environment

def main():
    # 添加当前目录到Python路径
    project_root = os.path.dirname(os.path.abspath(__file__))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    
    # 设置Django配置模块
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'frsit_eployment_.settings')
    
    # 初始化Django
    try:
        django.setup()
        print("Django setup successful!")
    except Exception as e:
        print(f"Django setup error: {e}")
        return False

    # 设置测试环境
    try:
        setup_test_environment()
        print("Test environment setup successful!")
    except Exception as e:
        print(f"Test environment setup error: {e}")
        return False

    # 测试hello视图
    try:
        c = Client()
        response = c.get('/practice/hello/')
        print('Status code:', response.status_code)
        print('Content:', response.content.decode())
        
        # 断言检查
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        assert 'Hello, Django!' in response.content.decode(), "Expected 'Hello, Django!' in response content"
        
        print('All tests passed!')
        return True
    except Exception as e:
        print(f"Test failed: {e}")
        return False

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)