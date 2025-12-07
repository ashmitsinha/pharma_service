from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def authView(request):
    if request.method == "POST":
        #form = UserCreationForm()
        form = UserCreationForm(request.POST or None)
        if form.is_Valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form":form})


# Create your views here.
@login_required
def home(request):
    #return HttpResponse("hello world")
    return(request, "registration/home.html")

