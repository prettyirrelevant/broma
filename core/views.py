from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET


@require_GET
def index(request: HttpRequest) -> HttpResponse:
    username = request.session.get("username")

    return render(request, "index.html", {"title": "Broma", "username": username})
