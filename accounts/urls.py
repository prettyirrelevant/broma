from django.urls import path

from . import views

app_name = "accounts"
urlpatterns = [
    path("pick_username/", views.pick_username, name="pick-username"),
]
