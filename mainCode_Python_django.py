#!/usr/bin/python3
import sys
from __save__ import *

########################################################
def runAllData(MyCodeTitle,MyCodeString,MyCodeName):
    global package1,package2,extension,count

    count = count + 1    

    (data1,data2,data3) = makeCode(MyCodeTitle,MyCodeString,MyCodeName+str(count))

    package1  = package1  + data1
    package2  = package2  + data2
    extension = extension + data3
########################################################


package1   = ""
package2   = ""
extension  = ""
count      = 0
MyCodeName = sys.argv[2]



# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Python django ( 範例 )"
# MyCodeString = '''
# ###  Python django 範例程式 ####
# ### file: mainCode_Python_django
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)



# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Python django ( 範例 )"
# MyCodeString = '''
# ###  Python django 範例程式 ####
# ### file: mainCode_Python_django
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)



# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Python django ( 範例 )"
# MyCodeString = '''
# ###  Python django 範例程式 ####
# ### file: mainCode_Python_django
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)



# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Python django ( 範例 )"
# MyCodeString = '''
# ###  Python django 範例程式 ####
# ### file: mainCode_Python_django
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)



### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Python django ( 基本設定 )"
MyCodeString = '''
###  Python django 基本設定 ####
### file: mainCode_Python_django

## 基本設定 settings.py
LANGUAGE_CODE = 'zh-hant'
TIME_ZONE = 'Asia/Taipei'

# 創建一個專案
django-admin startproject HelloJango

## ???
python manage.py migrate

# 啟動服務
python manage.py runserver
python manage.py runserver 0.0.0.0:8000


## 建立一個 app
python manage.py startapp app

## 修改 HelloJango/settings.py
## 把它加入 INSTALLED_APPS：
INSTALLED_APPS = [
    ... ,
    ... ,
    'app',
]

## 修改 HelloJango/urls.py
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('home/' , views.home,name='home'),
]


## 建立 app/templates 目錄
## 編輯 app/home.html


## 修改 app/views.py

from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("My Test")

def home(request):
    return render(request,'home.html')
    
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)









##### 這是輸出 ######################################
if sys.argv[1] == "package1":     print(package1)
if sys.argv[1] == "package2":     print(package2)
if sys.argv[1] == "extension":    print(extension)
##### END 這是輸出 ##################################
