from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


@csrf_exempt
def respond_to_hii(request):
    if request.method == 'POST':
        try:

            data = json.loads(request.body.decode('utf-8'))
            if data.get('message') == "Hii":
                return JsonResponse({'response': 'Hii'}, status=200)
            else:
                return JsonResponse({'error': 'Invalid message'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)
