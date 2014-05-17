# Create your views here.
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, render_to_response, RequestContext, HttpResponseRedirect

from account.models import Account
from account.forms import AccountCreateForm
from challenge.models import Challenge, Tag
from utils.func import get_account_from_user

from datetime import datetime

def index(request):
    template = 'index.html'

    form = AccountCreateForm(request.POST or None)
    context = RequestContext(request)

    if request.user.is_authenticated():
        current_account = get_account_from_user(request.user)

        if current_account is None:
            logout(request)
            redirect('/')
        else:
            pass

        return home(request)

    return render_to_response(template, locals(), context_instance=context)

@login_required
def home(request, challenge_id = None):
    template = 'home.html'

    challenges = Challenge.objects.all().order_by('start_date')[:4]
    now = datetime.now()

    for challenge in challenges:
        if challenge.start_date <= now.date() <= challenge.finish_date:
            print "123"
            challenge.active = True
        else:
            challenge.active = False

    if challenge_id is None:
        current_challenge = challenges[len(challenges)-1]
    else:
        current_challenge = Challenge.objects.get(id=chalenge_id)

    current_account = get_account_from_user(request.user)
    if current_challenge.post_set.filter(account = current_account):
        disable_create_btn = True
    else:
        disable_create_btn = False


    return render(request,
                  template,
                  {'challenges': challenges,
                   'disable_create_btn': disable_create_btn,
                   'current_challenge': current_challenge })

def about(request):
    pass
