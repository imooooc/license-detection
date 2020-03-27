# coding:utf-8
from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from django.shortcuts import render
import os
from vmoli.settings import MEDIA_ROOT
# Create your views here.
class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')



import chardet     # 获取上传文件编码格式
from django.views.decorators.csrf import csrf_exempt

class Uploads(View):
   """文件上传 类视图"""
   def get(self, request):
       """表单页面"""
       return render(request, "uploads.html")

   # @csrf_exempt
   # def post(self, request):
       # # 获取json文件对象
       # obj = request.FILES.get('file_name')
       # print('obj')
       # print(type(obj))
       # for chunk in obj.chunks():
       #     print(type(chunk))
       #     #ls = chardet.detect(chunk)
       #     print(chardet.detect(chunk))
       #     encoding = chardet.detect(chunk)['encoding']
       #     print(encoding)
       #     data = chunk.decode(encoding)
       #     print(data)
       # return HttpResponse('ok')

   def post(self, request):

       myFile = request.FILES.get("myfile", None)  # 获取上传的文件，如果没有文件，则默认为None
       if not myFile:
           return HttpResponse("no files for upload!")
       img_path = 'image/' + myFile.name
       destination = open(os.path.join(MEDIA_ROOT,img_path), 'wb+')  # 打开特定的文件进行二进制的写操作
       for chunk in myFile.chunks():  # 分块写入文件
           destination.write(chunk)
       destination.close()
       data = ''
       return render(request, 'response.html', {data:'data'})


