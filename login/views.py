from django.shortcuts import render

from .forms import LoginForm

def index(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data.get('email'))
            print(form.cleaned_data.get('password'))

    else:
        form = LoginForm()

    return render(request, "login/index.html", { "form": form })

