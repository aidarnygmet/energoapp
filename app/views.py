from django.shortcuts import render
from .models import ugol
import json
from django.http import JsonResponse
# Create your views here.
def base(request):
    return render(request, 'base.html')
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

