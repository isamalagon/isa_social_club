from django.http import JsonResponse

places = [
    "Pyramids of Giza",
    "Luxor Temple",
    "Nile River Felucca",
    "Karnak Temple",
    "Saqqara",
    "Khan el-Khalili Market"

]

def list_places(request):
    return JsonResponse({"places": places})
