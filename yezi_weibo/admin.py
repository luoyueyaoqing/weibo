from django.contrib import admin
from .models import WBUser, WBText, WeiBo, Comment


admin.site.register(WBUser)
admin.site.register(WBText)
admin.site.register(WeiBo)
admin.site.register(Comment)