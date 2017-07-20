"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#from django.conf.urls import url
#from django.contrib import admin

#urlpatterns = [
#    url(r'^admin/', admin.site.urls),
#]
from django.contrib import admin
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from Employee.views import EmployeeViewSet
from Event.views import EventViewSet
from Registered_Events.views import Registered_Events_Viewset

router = DefaultRouter()
router.register(prefix='employees', viewset=EmployeeViewSet)
router.register(prefix='event', viewset=EventViewSet)
router.register(prefix='register-events',viewset=Registered_Events_Viewset)
urlpatterns = [
   url(r'^admin/', admin.site.urls),
]
urlpatterns += router.urls
