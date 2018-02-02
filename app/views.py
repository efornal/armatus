# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from datetime import datetime
from datetime import timedelta
from django.contrib.auth.decorators import login_required

# Create your views here.


def default_date_from():
    return datetime.now().strftime('%d-%m-%Y %H:%M')



def set_language(request, lang='es'):
    if 'lang' in request.GET:
        lang = request.GET['lang']
    translation.activate(lang)
    request.session[translation.LANGUAGE_SESSION_KEY] = lang
    logging.info("Language changed by the user to '{}'".format(lang))
    return redirect('index')


# @login_required
# def application_new(request):
#     form = ApplicationForm()
#     context = {'form': form,
#                'date_from': default_date_from(),
#                'date_until': default_date_until()}
#     return render(request, 'application/new.html', context)


# @login_required
# def application_list(request):
#     applications = Application.objects.filter(user=request.user.pk)
#     context = {'applications': applications}
#     return render(request, 'application/index.html', context)


# @login_required
# def application_show(request, pk):
#     application = Application.objects.get(pk=pk)
#     form = ApplicationForm(instance=application)
#     context = {'application': application, 'form': form}
#     return render(request, 'application/show.html', context)


@login_required
def index(request):
    context={}
    return render(request, 'index.html', context)
