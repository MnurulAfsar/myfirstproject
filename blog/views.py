from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<h1> Welcome to Django Tutorial </h1>")


def about_us(request):
    return HttpResponse(
        "<h1> About Us </h1><br><p> Lorem Ipsum is simply dummy text of the printing "
        "and typesetting industry. Lorem Ipsum has been the industry's standard dummy "
        "text ever since the 1500s, when an unknown printer took a galley of type and "
        "scrambled it to make a type specimen book. It has survived not only five centuries, "
        "but also the leap into electronic typesetting, remaining essentially unchanged. "
        "It was popularised in the 1960s with the release of Letraset sheets containing "
        "Lorem Ipsum passages, and more recently with desktop publishing software like "
        "Aldus PageMaker including versions of Lorem Ipsum.</p>")


def contact_us(request):
    return HttpResponse(
        "<h1> contact Us </h1><br><p> Lorem Ipsum is simply dummy text of the printing "
        "and typesetting industry. Lorem Ipsum has been the industry's standard dummy "
        "text ever since the 1500s, when an unknown printer took a galley of type and "
        "scrambled it to make a type specimen book. It has survived not only five centuries, "
        "but also the leap into electronic typesetting, remaining essentially unchanged. "
        "It was popularised in the 1960s with the release of Letraset sheets containing "
        "Lorem Ipsum passages, and more recently with desktop publishing software like "
        "Aldus PageMaker including versions of Lorem Ipsum.</p>")



