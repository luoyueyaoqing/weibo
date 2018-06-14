from django.shortcuts import render, HttpResponse
from .models import WBText, WBUser


def index(request):
    weibos = WBText.objects.all()
    return render(request, 'yezi_weibo/index.html', {'weibos': weibos})


def update(request):
    # if request.method == 'POST':
    #     author = WBUser.objects.get(.username)
    #     msg = request.POST.get('msg')
    #     wbt = WBText.objects.create(author=author, msg=msg)
    #     wbt.save()
    #     weibos = WBText.objects.all()
    #     return render(request, 'yezi_weibo/index.html', {'weibos': weibos})

    return render(request, 'yezi_weibo/update.html')


