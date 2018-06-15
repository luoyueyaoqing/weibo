from django.shortcuts import render
from yezi_weibo.models import WBUser


def index(request):
    users = WBUser.objects.all()
    return render(request, 'index.html', {'users': users})