from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import WBText, WBUser
from django.contrib.auth.decorators import login_required


@login_required
def homepage(request):
    # wb_user = WBUser.objects.get(id=request.user.id)
    wb_user = get_object_or_404(WBUser, id=request.user.id)
    return render(request, 'yezi_weibo/homepage.html', {
        'wb_user': wb_user})


def user_page(request):
    uid = request.GET.get('uid')
    wb_user = get_object_or_404(WBUser, id=uid)
    return render(request, 'yezi_weibo/user_page.html', {
        'wb_user': wb_user})


def update(request):
    # if request.method == 'POST':
    #     author = WBUser.objects.get(.username)
    #     msg = request.POST.get('msg')
    #     wbt = WBText.objects.create(author=author, msg=msg)
    #     wbt.save()
    #     weibos = WBText.objects.all()
    #     return render(request, 'yezi_weibo/index.html', {'weibos': weibos})

    return render(request, 'yezi_weibo/update.html')
