from django.shortcuts import render, HttpResponse,get_object_or_404, redirect, HttpResponseRedirect
from .models import WBText, WBUser, WeiBo, Comment
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
    if request.method == "POST":
        msg = request.POST.get('msg')
        wbt = WBText.objects.create(author=wb_user, msg=msg)
        wb = WeiBo.objects.create(user=wb_user, text=wbt)
        return HttpResponseRedirect('/')
    return render(request, 'yezi_weibo/update.html', {'wb_user': wb_user})


def wb_comment(request):
    request.session['login_from'] = request.META.get('HTTP_REFERER', '/')
    wid = request.POST.get('wid')
    wb = get_object_or_404(WeiBo, id=wid)
    wb_user = get_object_or_404(WBUser, id=request.user.id)
    msg = request.POST.get('msg')
    comment = wb.comment_this(user=wb_user, text=msg)
    return HttpResponseRedirect(request.session['login_from'])

