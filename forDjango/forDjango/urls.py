"""
URL configuration for forDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from askme import views

urlpatterns = [
    path('', views.mainPage, name = "mainPage"),
    path('admin/', admin.site.urls),
    path('answerPage/<int:id>/', views.answerPage, name = "answerPage"),
    path('mainPage', views.mainPage, name = "mainPage"),
    path('askQuestPage', views.askQuestPage, name = "askQuest"),
    path('logInPage', views.logInPage, name = "login"),
    path('registrationPage', views.registrationPage, name = "register"),
    path('searchingByTagPage/<str:tag_name>', views.searchingByTagPage, name = "tag_page"),
    path('settingsPage', views.settingsPage, name = "settings"),
]
