from django.http import JsonResponse

def profile(request):
    return JsonResponse({
        "name": "Traveler",
        "destination": "Egypt",
        "status": "excited"
   })

