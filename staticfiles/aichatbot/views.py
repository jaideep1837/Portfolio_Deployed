from django.shortcuts import render

def chatbot(request):
    return render(request, "index.html")