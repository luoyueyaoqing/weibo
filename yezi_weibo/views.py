from django.shortcuts import render, HttpResponse,get_object_or_404, redirect, HttpResponseRedirect
from .models import WBText, WBUser, WeiBo
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
    wbs = WeiBo.objects.filter(user=wb_user).order_by('-time_create')
    return render(request, 'yezi_weibo/user_page.html', {
        'wb_user': wb_user,
        'wbs': wbs,
    })


def wb_update(request):
    wb_user = get_object_or_404(WBUser, id=request.user.id)
    print('===========', wb_user)
    if request.method == "POST":
        msg = request.POST.get('msg')
        wbt = WBText.objects.create(author=wb_user, msg=msg)
        wb = WeiBo.objects.create(user=wb_user, text=wbt)
        return HttpResponseRedirect('/')
    return render(request, 'yezi_weibo/update.html', {'wb_user': wb_user})
