from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views import generic
from rest_framework.decorators import api_view
from django.contrib.auth import login, authenticate, mixins
from django.shortcuts import render, redirect
from apps.web.forms import SignUpForm
from rest_framework.authtoken.models import Token


def index(request):
    context = {'title': 'Project Noe'}
    return render(request, 'web/index.html', context=context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('web/dashboard/')
    else:
        form = SignUpForm()
    return render(request, 'web/sign_up.html', {'form': form})


@login_required
def createBasicApiToken(request):
    if request.method == 'POST':
        return JsonResponse(data=Token.objects.create(user=request.user))
    else:
        return redirect('/')


class DashboardView(mixins.LoginRequiredMixin, generic.TemplateView):
    template_name = 'web/dashboard.html'

    def get_context_data(self, **kwargs):
        kwargs['title'] = 'Dashboard'
        return super().get_context_data(**kwargs)
