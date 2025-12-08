#!/usr/bin/env python
"""
Test script for the hello view
"""
import os
import sys
import django
from django.test import Client

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'frsit_eployment_.settings')
django.setup()

# Test the hello view
c = Client()
response = c.get('/practice/hello/')
print('Status code:', response.status_code)
print('Content:', response.content.decode())

# Assertions
assert response.status_code == 200
assert 'Hello, Django!' in response.content.decode()

print('All tests passed!')