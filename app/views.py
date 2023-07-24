from django.shortcuts import render, get_object_or_404, redirect
from .models import ugol, kotel_status, kotel_info
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
# Create your views here.
def base(request):
    return render(request, 'base.html')
def demo(request):
    return render(request, 'demo.html')

@csrf_exempt 
def save_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            value = data.get('value')
            if value is not None:
                ugol_object = ugol(value=value)
                ugol_object.save()
                return JsonResponse({'success': True})
            else:
                # Handle the case when the value is not provided or is invalid
                return JsonResponse({'success': False, 'message': 'Invalid value'})
        except json.JSONDecodeError:
            # Handle the case when the request body is not valid JSON
            return JsonResponse({'success': False, 'message': 'Invalid JSON data'})
  
    return JsonResponse({'message': 'Invalid request.'})

@csrf_exempt 
def save_kotel_status(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            kotel_id = data.get('id')
            kotel_status_sost = data.get('status')
            begin = data.get('begin')
            if kotel_id is not None and kotel_status is not None and begin is not None:
                status_object = kotel_status(kotel_id = kotel_id, kotel_status = kotel_status_sost, begin = begin)
                status_object.save()
                object_id = status_object.id
                response_data = {'object_id': object_id}
                return JsonResponse(response_data)
        except json.JSONDecodeError:
            # Handle the case when the request body is not valid JSON
            return JsonResponse({'success': False, 'message': 'Invalid JSON data'})
    return JsonResponse({'message': 'Invalid request.'})

@csrf_exempt 
def update_kotel_status(request, object_id):
    object = kotel_status.objects.get(id = object_id)
    if request.method == 'PUT':
        data = json.loads(request.body)
        object.end = data.get('end')
        object.save()
        return JsonResponse({'success': True})
    return JsonResponse({'message': 'Invalid request.'})

@csrf_exempt 
def save_kotel_info(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            kotel_id = data.get('kotel_id')
            ugol_con = data.get('ugol_con')
            mazut_con = data.get('mazut_con')
            par = data.get('par')
            temp = data.get('temp')
            pressure = data.get('pressure')
            goal_temp = data.get('goal_temp')
            time = data.get('time')
            parTotal = data.get('parTotal')
            status = data.get('status')
            f1 = data.get('f1')
            f2 = data.get('f2')
            f3 = data.get('f3')
            f4 = data.get('f4')

            if kotel_id is not None:
                kotel_info_object = kotel_info(kotel_id = kotel_id, ugol_con = ugol_con, mazut_con=mazut_con, par=par, temp=temp, pressure=pressure,
                                         goal_temp = goal_temp, time = time, parTotal = parTotal, status= status, f1=f1,f2=f2,f3=f3,f4=f4)
                kotel_info_object.save()
                return JsonResponse({'success': True})
            else:
                # Handle the case when the value is not provided or is invalid
                return JsonResponse({'success': False, 'message': 'Invalid value'})
        except json.JSONDecodeError:
            # Handle the case when the request body is not valid JSON
            return JsonResponse({'success': False, 'message': 'Invalid JSON data'})

    return JsonResponse({'message': 'Invalid request.'})
def graph_data(request):
    data = ugol.objects.all().values('value', 'timestamp')
    formatted_data = [{'value': item['value'], 'timestamp': item['timestamp']} for item in data]

    return JsonResponse(formatted_data, safe=False)
def update_graph(request):
    # Retrieve the data from the model
    data = ugol.objects.all().values('value', 'timestamp')

    # Convert the data to a suitable format (e.g., a list of dictionaries)
    graph_data = [
        {'value': entry.value, 'timestamp': entry.timestamp.isoformat()}
        for entry in data
    ]
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'graph_group',  # Group name to target connected clients
        {
            'type': 'send_update',
            'data': graph_data,
        }
    )
    return HttpResponse('Update successful!')