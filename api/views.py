from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def hello(request):
    return JsonResponse({
        "message": "Hello from Django on Vercel!",
        "status": "success"
    })
