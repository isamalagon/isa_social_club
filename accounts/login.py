from django.http import JsonResponse

def login(request):
    username = request.GET.get("username", "guest")
    return JsonResponse({
        "welcome": username,
        "status": "logged in (not real auth yet)"
    })
