from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'update/$', views.wb_update, name='update'),
    url(r'user_page/$', views.user_page, name='user_page'),
    url(r'wb_comment/$', views.wb_comment, name='wb_comment'),
]