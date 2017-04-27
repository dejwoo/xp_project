from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from apps.web.forms import SignUpForm


def index(request):
    context = {'title': 'Project Noe'}
    return render(request, 'web/index.html', context=context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.company = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('web/')
    else:
        form = SignUpForm()
    return render(request, 'web/sign_up.html', {'form': form})


@login_required
def logged_in(request):
    context = {'title': 'Dashboard'}
    return render(request, 'web/dashboard.html', context=context)
