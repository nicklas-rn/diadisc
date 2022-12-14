from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.template.loader import render_to_string
from .utils import *
from .models import *


def home(request):

    try:
        code = request.GET["code"]
    except:
        code = ''

    context = {
        'code': code,
    }

    return render(request, 'home.html', context)


def create_waitlist_user(request):

    print(request.POST['email'], request.POST['code'])

    waitlist_user = WaitlistUser.objects.filter(email=request.POST['email']).first()
    if not waitlist_user:
        waitlist_user = WaitlistUser.objects.create(
            email=request.POST['email'],
            code=generateId(6),
        )

        inviting_user = WaitlistUser.objects.filter(code=request.POST['code']).first()
        print(inviting_user)
        if inviting_user:
            inviting_user.invited_users += f'{waitlist_user.email} '
            inviting_user.save()

    context = {
        'code': waitlist_user.code,
        'count': waitlist_user.id,
    }

    html = render_to_string('waitlist_success.html', context),

    return JsonResponse(html, safe=False)
