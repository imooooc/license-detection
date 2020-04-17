"""
-*- coding:utf-8 -*-
Author: Zhu Chen
Organization: 07 LP detection group
Create Time: 2020/04  All rights reserved
WSGI config for vmoli_com project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vmoli_com.settings')

application = get_wsgi_application()
