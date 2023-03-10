from django.shortcuts import render
from .models import News


def index(request):
    news = News.objects.all()[:2]
    context = {"news": news}
    return render(request, "pages/index.html", context)


def tos(request):
    return render(request, "pages/tos.html", {})


def privacy(request):
    return render(request, "pages/privacy.html", {})
