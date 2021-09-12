from django.urls import path

from . import views

app_name = "chats"
urlpatterns = [
    path("", views.index, name="index"),
    path("create_conversation", views.create_conversation, name="create-conversation"),
]
