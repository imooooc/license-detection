#-*- coding:utf-8 -*-# Author: Zhu Chen # Organization: 07 LP detection group# Create Time: 2020/03  All rights reservedimport xadminfrom xadmin import viewsfrom .models import Userclass UserAdmin(object):    list_display = ['openid', 'stu_id', 'pwd', 'name', 'create_time']    search_fields = ['openid', 'stu_id', 'pwd', 'name']    list_filter = ['openid', 'stu_id', 'pwd', 'name', 'create_time']class BaseSetting(object):    enable_themes = False    use_bootswatch = Falseclass GlobalSettings(object):    site_title = "吊销车牌特案组后台管理系统"    site_footer = "www.vmoli.com"    #menu_style = "accordion"xadmin.site.register(User, UserAdmin)xadmin.site.register(views.BaseAdminView, BaseSetting)xadmin.site.register(views.CommAdminView, GlobalSettings)