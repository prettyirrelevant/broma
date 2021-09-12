from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST

from .models import Conversation, User


@require_GET
def index(request: HttpRequest) -> HttpResponse:
    username = request.session.get("username")

    return render(request, "index.html", {"title": "Broma", "username": username})


@require_POST
def create_conversation(request: HttpRequest) -> JsonResponse:
    session_username = request.session.get("username")
    if not session_username:
        return JsonResponse(
            {"status": False, "message": "No username found in session!"}, status=422
        )

    try:
        user: User = User.objects.get(username=session_username)
    except User.DoesNotExist as error:
        return JsonResponse({"status": False, "message": str(error)}, status=400)

    new_conversation: Conversation = Conversation.objects.create(creator=user)

    return JsonResponse(
        {
            "status": True,
            "message": "Conversation created successfully!",
            "data": {"conversation_id": new_conversation.id},
        },
        status=201,
    )


@require_POST
def join_conversation(request: HttpRequest) -> JsonResponse:
    ...
