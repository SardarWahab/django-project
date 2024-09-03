from django.contrib import admin
from django.urls import path
from stdapp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('/',home, name='home'),
    path('student/<int:Roll_No>',student_detail )
]
