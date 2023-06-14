from django.shortcuts import render


def first_view(request):
    return render(request, "first_view.html")


def second_view(request):
    return render(request, "second_view.html")


def third_view(request):
    return render(
        request,
        "third_view.html",
        {"name": "Milenko Castillo", "location": "Puente Alto"},
    )


def fourth_view(request):
    return render(request, "fourth_view.html")
