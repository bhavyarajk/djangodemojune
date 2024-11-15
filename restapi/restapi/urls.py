"""
URL configuration for restapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from  students import views
from rest_framework.routers import SimpleRouter
from rest_framework.authtoken import views as rview  #module aliasing
router=SimpleRouter()
router.register('students',views.StudentView)
router.register('users',views.RegisterView)#Register View

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.studentlist,name="students"),
    # path('studentdetail',views.studentdetail,name="details"),
# path('',views.StudentListView.as_view(),name="students"),
#     path('studentdetail/<int:pk>',views.StudentDetailView.as_view(),name='details')
path("",include(router.urls)),
    path('search',views.SearchView.as_view()),
    path('searchname',views.SearchName.as_view()),
    path('api-token-auth/', rview.obtain_auth_token), #login view
    path('logout',views.LogoutAPIView.as_view()) #Logout view
]
