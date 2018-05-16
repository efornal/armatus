from django.shortcuts import render
from datetime import datetime
from datetime import timedelta
from .models import Check
from .models import Service
from .forms import CheckForm
from django.contrib.auth.decorators import login_required
from django.utils import translation
import logging
from django.shortcuts import redirect
from django.db import transaction
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.core.exceptions import ObjectDoesNotExist


def set_language(request, lang='es'):
    if 'lang' in request.GET:
        lang = request.GET['lang']
    translation.activate(lang)
    request.session[translation.LANGUAGE_SESSION_KEY] = lang
    logging.info("Language changed by the user to '{}'".format(lang))
    return redirect('index')


@login_required
def checks_new(request):
    form = CheckForm()
    try:
        latest_check = Check.objects.latest('created_at')
        clean_tank_value = unicode(latest_check.tank).replace(",",".")
        defaults = {
            'tank': clean_tank_value,
            'operating_hours': latest_check.operation_hours(),
            'starts':latest_check.starts+1,
            'voltage_1': latest_check.voltage_1,
            'voltage_2': latest_check.voltage_2,
            'voltage_3': latest_check.voltage_3
        }
        form = CheckForm(initial=defaults)
    except ObjectDoesNotExist, e:
        form = CheckForm()
    except Exception, e:
        logging.error(e)

    context = {'form': form,}
    return render(request, 'checks/new.html', context)


def sanitize_checks_create_params(request):
    params = request.POST.copy()
    try:
        params['user'] = request.user.pk
        params['start_time'] = datetime.now().strftime('%H:%M')
    except Exception, e:
        logging.error('ERROR Exception',e)
    return params


@login_required
def checks_create(request):
    params = sanitize_checks_create_params(request)
    form = CheckForm(params)
    context = {}
    logging.warning(params)
    if form.is_valid():
        context.update({'form': form,})
        try:
            logging.warning("creating new check..")
            check = form.save()
            messages.info(request, _('msg_check_created'))
            return redirect('index')
        except Exception as e:
            logging.error(e)
    else:
        logging.warning("ERROR creating new check..")
        logging.error(form.errors)
        context.update({'form': form,})

    return render(request, 'checks/new.html', context)


@login_required
def checks_show(request, pk):
    check = Check.objects.get(pk=pk)
    form = CheckForm(instance=check)
    clean_tank_value = float(check.tank)
    context = {'check': check, 'form': form, 'clean_tank_value': clean_tank_value}
    return render(request, 'checks/show.html', context)


@login_required
def checks_finalize(request, pk):
    try:
        check = Check.objects.get(pk=pk)
        if not check.end_time:
            check.end_time = unicode(datetime.now().strftime('%H:%M'))
            check.save(update_fields=["end_time"])
        else:
            logging.error('The check {} has already been finalized'.format(pk))
    except Exception as e:
        logging.error(e)
    return redirect('index')


@login_required
def index(request):
    context={}
    checks = Check.objects.all().order_by('-created_at')
    context = {'checks': checks}
    return render(request, 'index.html', context)


@login_required
def services_index(request):
    context={}
    services = Service.objects.all().order_by('-created_at')
    context = {'services': services}
    return render(request, 'services/index.html', context)
