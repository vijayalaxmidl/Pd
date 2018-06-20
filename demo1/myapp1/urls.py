from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^index/',views.register,name='index'),
	url(r'^show/',views.show,name='show'),
	url(r'^simpleemail/(?P<))
]