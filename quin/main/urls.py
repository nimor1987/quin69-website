from django.urls import path
from .views import index, privacy, tos


urlpatterns = [
    path("", index, name="index"),
    path("terms-and-conditions", tos, name="tos"),
    path("privacy-policy", privacy, name="privacy"),
]
