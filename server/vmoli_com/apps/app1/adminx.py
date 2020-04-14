# -*- coding:utf-8 -*-
# Author: Zhu Chen
# Organization: 07 LP detection group
# Create Time: 2020/03  All rights reserved
import xadmin
from .models import UserProfile, EmailVeriRecord


class UserProfileAdmin(object):
    list_display = ['user_name', 'email', 'password', 'create_time', 'is_active']
    search_fields = ['user_name', 'email', 'password', 'is_active']
    list_filter = ['user_name', 'email', 'password', 'create_time', 'is_active']


class EmailVeriRecordAdmin(object):
    list_display = ['code', 'email', 'send_time', 'expire_time', 'email_type']
    search_fields = ['code', 'email', 'send_time', 'expire', 'email_type']
    list_filter = ['code', 'email', 'send_time', 'expire_time', 'email_type']


xadmin.site.register(UserProfile, UserProfileAdmin)
xadmin.site.register(EmailVeriRecord, EmailVeriRecordAdmin)
