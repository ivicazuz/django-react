from django.http import JsonResponse
from datetime import datetime


def index(request):
    current_time = datetime.now().strftime("%H:%M:%S")
    current_date = datetime.now().strftime("%A %m %-Y")

    data = {
        "time": current_time,
        "date": current_date,
    }

    return JsonResponse(data)
