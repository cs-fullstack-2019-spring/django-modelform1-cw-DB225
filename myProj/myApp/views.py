from django.shortcuts import render
from django.http import HttpResponse
from .forms import NewBlog


# This page will handles the landing page
def index(request):
    return render(request, 'myApp/index.html')

# This page will provide a form to add users
def blog(request):
    formToSend = NewBlog()
    if request.method == "POST":
        print("Post Confirmed!!")
        formToSend = NewBlog(request.POST)
        if formToSend.is_valid():
            formToSend.save(commit=True)
            return index(request)
    else:
        print("ERROR")
    return render(request, 'myApp/userPage.html', {"form": formToSend})
