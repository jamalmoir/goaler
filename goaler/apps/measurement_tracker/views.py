import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.utils import timezone

from .forms import MeasurementForm
from .models import Measurement


@login_required
def history(request):
    latest_measurements = Measurement.objects.filter(user=request.user).order_by('-date')[:30]

    types = ['weight', 'neck', 'chest', 'arm', 'waist', 'hip', 'thigh']
    colors = ['#990000', '#999900', '#009900', '#990099', '#000099', '#660099', '#996600']
    datasets = []

    dates = [date[0].isoformat() for date in list(latest_measurements.values_list('date'))]

    for i, t in enumerate(types):
        measurements = [m[0] for m in list(latest_measurements.values_list(t))]
        data_points = [{'x': dates[i], 'y': measurements[i]} for i in reversed(range(len(measurements)))]
        datasets.append({
            'label': t.title(),
            'data': data_points,
            'lineTension': 0,
            'borderColor': colors[i],
            'backgroundColor': colors[i],
            'fill': False,
        })

    labels = [date[0].strftime('%Y/%m/%d') for date in list(latest_measurements.values_list('date'))]
    labels = list(set(labels))

    data = {
        'labels': labels,
        'datasets': datasets
    }

    options = {
        'responsive': True,
        'title': {
            'display': True,
            'text': 'Measurement History',
        },
        'tooltips': {
            'mode': 'index',
            'intersect': False,
        },
        'hover': {
            'mode': 'nearest',
            'intersect': True,
        },
        'scales': {
            'xAxes': [{
                'display': True,
                'scaleLabel': {
                    'display': True,
                    'labelString': 'Date',
                },
            }],
            'yAxes': [{
                'display': True,
                'scaleLabel': {
                    'display': True,
                    'labelString': 'Weight | Circumference',
                }
            }],
        }
    }

    data = json.dumps(data)
    options = json.dumps(options)

    template = loader.get_template('measurement_tracker/history.html')
    context = {
        'latest_measurements': latest_measurements,
        'chart_data': data,
        'chart_options': options,
    }

    return HttpResponse(template.render(context, request))


@login_required
def add(request):
    if request.method == 'POST':
        form = MeasurementForm(request.POST)

        if form.is_valid():
            measurement = form.save(commit=False)
            measurement.user = request.user
            measurement.date = timezone.now()
            measurement.save()

            return redirect('measurement_tracker:history')
    template = loader.get_template('measurement_tracker/add.html')
    context = {
        'today': timezone.now().date,
        'form': MeasurementForm(),
    }

    return HttpResponse(template.render(context, request))
