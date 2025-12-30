from django.http import JsonResponse


def welcome(request):
    return JsonResponse({
        "club": "Isa Social Club",
        "message": "Welcome traveler! This API is for people planning trips to Egypt",
        "note": "still working on more features"
    })


# temporary list for now 
egypt_tips = [
    {"id": 1, "tip": "Buy a local SIM card at the airport"},
    {"id": 2, "tip": "Carry small bills for tipping"},
    {"id": 3, "tip": "Visit the pyramids early morning"},
]


def show_tips(request):
    data = {
        "tips": egypt_tips,
        "total": len(egypt_tips)
    }
    return JsonResponse(data)


def add_tip(request):
    if request.method == "POST":
        tip_text = request.POST.get("tip")

        if tip_text == "" or tip_text is None:
            return JsonResponse({
                "error": "Tip cannot be empty"
            })

        new_tip = {
            "id": len(egypt_tips) + 1,
            "tip": tip_text
        }

        egypt_tips.append(new_tip)

        return JsonResponse({
            "message": "Tip added",
            "tip": new_tip
        })

    return JsonResponse({
        "error": "Only POST requests allowed"
    })
