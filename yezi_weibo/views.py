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
    user = get_object_or_404(WBUser, id=request.user.id)
    uid = request.GET.get('uid')
    wb_user = get_object_or_404(WBUser, id=uid)
    wbs = WeiBo.objects.filter(user=wb_user).order_by('-time_create')
    return render(request, 'yezi_weibo/user_page.html', {
        'wb_user': wb_user,
        'wbs': wbs,
        'user': user,
    })


@login_required
def wb_update(request):
    # 发表微博
    wb_user = get_object_or_404(WBUser, id=request.user.id)
    if request.method == "POST":
        msg = request.POST.get('msg')
        wbt = WBText.objects.create(author=wb_user, msg=msg)
        wb = WeiBo.objects.create(user=wb_user, text=wbt)
        return HttpResponseRedirect('/')
    return render(request, 'yezi_weibo/update.html', {'wb_user': wb_user})


@login_required
def wb_comment(request):
    # 评论微博
    request.session['login_from'] = request.META.get('HTTP_REFERER', '/')
    wid = request.POST.get('wid')
    wb = get_object_or_404(WeiBo, id=wid)
    wb_user = get_object_or_404(WBUser, id=request.user.id)
    msg = request.POST.get('msg')
    comment = wb.comment_this(user=wb_user, text=msg)
    return HttpResponseRedirect(request.session['login_from'])


@login_required
def wb_delete(request):
    # 删除微博
    request.session['login_from'] = request.META.get('HTTP_REFERER', '/')
    wid = request.GET.get('wid')
    wb = get_object_or_404(WeiBo, id=wid)
    # wb.delete()
    wb.del_this()
    return HttpResponseRedirect(request.session['login_from'])


@login_required
def user_follow(request):
    # 用户关注
    user = get_object_or_404(WBUser, id=request.user.id)
    uid = request.GET.get('uid')
    wb_user = get_object_or_404(WBUser, id=uid)
    user.follow(wb_user)
    return HttpResponse()