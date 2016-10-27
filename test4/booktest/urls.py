from django.conf.urls import url
from . import views
urlpatterns = [

	url(r"^cityTest/$",views.cityTest,name="cityTest"),
	url(r'^pro/$', views.pro, name='pro'),
	url(r'^pro(?P<id>[0-9]+)/$',views.pro2,name = "pro2"),
]