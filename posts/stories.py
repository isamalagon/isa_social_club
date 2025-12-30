from django.http import JsonResponse

stories = []

def add_story(request):
    if request.method == "POST":
        text = request.POST.get("story", "")
        stories.append(text)
        return JsonResponse({"message": "story added", "story": text})
    return JsonResponse({"error": "POST only"})

def list_stories(request):
    return JsonResponse({"stories": stories})
