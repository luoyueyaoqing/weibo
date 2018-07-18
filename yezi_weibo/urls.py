from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'update/$', views.wb_update, name='update'),
    url(r'wb_delete/$', views.wb_delete, name='wb_delete'),
    url(r'user_page/$', views.user_page, name='user_page'),
    url(r'wb_comment/$', views.wb_comment, name='wb_comment'),
    url(r'user_follow/$', views.user_follow, name='user_follow'),
    url(r'user_unfollow/$', views.user_unfollow, name='user_unfollow'),
    url(r'^forward/$', views.wb_forward, name='forward'),
]