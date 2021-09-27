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
from django.conf import settings
from datetime import date

def set_language(request, lang='es'):
    if 'lang' in request.GET:
        lang = request.GET['lang']
    translation.activate(lang)
    request.session[translation.LANGUAGE_SESSION_KEY] = lang
    logging.info("Language changed by the user to '{}'".format(lang))
    return redirect('index')

@login_required
def dashboard(request):
    fcc = settings.FUEL_CONSUMPTION_COEFFICIENT
    th_warning_tank = settings.THRESHOLD_WARNING_TANK
    th_danger_tank  = settings.THRESHOLD_DANGER_TANK
    th_warning_service = settings.THRESHOLD_WARNING_SERVICE
    th_danger_service  = settings.THRESHOLD_DANGER_SERVICE
    check = Check.objects.all().order_by('-created_at').first()
    service = Service.objects.filter(next_service_date__gte=date.today()) \
                             .order_by('-created_at').first()
    tests_performed = Check.objects.all().count()
    remaining_hours = round(check.tank*fcc,1)

    tank_color="#3399f3"
    if check.tank < th_warning_tank:
        tank_color="#D47500"
    if check.tank <= th_danger_tank:
        tank_color="#CD0200"

    service_color = "#3399f3"
    next_service_diff = None
    if service:
        next_service_diff = service.next_service_date - date.today()
        if next_service_diff.days < th_warning_service:
            service_color = "#D47500"
        if next_service_diff.days < th_danger_service:
            service_color = "#CD0200"
        if next_service_diff.days < 0:
            service_color = "#777"

        
    context = {'check': check,
               'service': service,
               'service_color': service_color,
               'next_service_diff': next_service_diff,
               'tank_color': tank_color,
               'tests_performed': tests_performed,
               'remaining_hours': remaining_hours}
    return render(request, 'dashboard.html', context)

@login_required
def checks_new(request):
    form = CheckForm()
    try:
        latest_check = Check.objects.latest('created_at')
        clean_tank_value = str(latest_check.tank).replace(',','.')
        defaults = {
            'tank': clean_tank_value,
            'operating_hours': latest_check.operation_hours(),
            'starts':latest_check.starts+1,
            'voltage_1': latest_check.voltage_1,
            'voltage_2': latest_check.voltage_2,
            'voltage_3': latest_check.voltage_3
        }
        form = CheckForm(initial=defaults)
    except ObjectDoesNotExist as e:
        form = CheckForm()
    except Exception as e:
        logging.error(e)

    context = {'form': form,}
    return render(request, 'checks/new.html', context)


def sanitize_checks_create_params(request):
    params = request.POST.copy()
    try:
        params['user'] = request.user.pk
        params['start_time'] = datetime.now().strftime('%H:%M')
    except Exception as e:
        logging.error('ERROR Exception',e)
    return params


@login_required
def checks_create(request):
    params = sanitize_checks_create_params(request)
    form = CheckForm(params)
    context = {}
    if form.is_valid():
        context.update({'form': form,})
        try:
            logging.warning("creating new check..")
            logging.info(params)
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
            check.end_time = str(datetime.now().strftime('%H:%M'))
            check.save(update_fields=["end_time"])
        else:
            logging.error('The check {} has already been finalized'.format(pk))
    except Exception as e:
        logging.error(e)
    return redirect('index')

@login_required
def index(request):
    return redirect('dashboard')

@login_required
def checks_index(request):
    context={}
    checks = Check.objects.all().order_by('-created_at')
    context = {'checks': checks}
    return render(request, 'checks/index.html', context)


@login_required
def services_index(request):
    context={}
    services = Service.objects.all().order_by('-created_at')
    context = {'services': services}
    return render(request, 'services/index.html', context)
