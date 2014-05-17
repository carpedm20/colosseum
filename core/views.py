# Create your views here.
from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, render_to_response, RequestContext, HttpResponseRedirect

from account.models import Account
from account.forms import AccountCreateForm
from challenge.models import Challenge, Tag
from utils.func import get_account_from_user

def index(request):
    index_template = 'index.html'
    home_template = 'home.html'

    form = AccountCreateForm(request.POST or None)
    context = RequestContext(request)

    if request.user.is_authenticated():
        current_account = get_account_from_user(request.user)

        if current_account is None:
            logout(request)
            redirect('/')
        else:
            pass

        return render(request,
                      home_template,
                      {})

    return render_to_response(index_template, locals(), context_instance=context)

def about(request):
    pass
