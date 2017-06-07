from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.views import generic
from rest_framework.decorators import api_view
from django.contrib.auth import login, authenticate, mixins
from django.shortcuts import render, redirect, render_to_response
from apps.web.forms import SignUpForm
from rest_framework.authtoken.models import Token
from rest_framework_jwt.settings import api_settings
from xp_project.settings.common import LOGIN_REDIRECT_URL


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
            return redirect(LOGIN_REDIRECT_URL)
    else:
        form = SignUpForm()
    return render(request, 'web/sign_up.html', {'form': form})


@login_required
def createBasicApiToken(request):
    if request.is_ajax() and request.method == 'POST':
        token = Token.objects.get_or_create(user=request.user)
        return JsonResponse(data={'token': token[0].key, 'isCreated': token[1]})
    else:
        return redirect('/')
@login_required
def createJwtApiToken(request):
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    payload = jwt_payload_handler(request.user)
    token = jwt_encode_handler(payload)
    return JsonResponse(data={'token':token})
class DashboardView(mixins.LoginRequiredMixin, generic.TemplateView):
    template_name = 'web/dashboard.html'

    def get_context_data(self, **kwargs):
        kwargs['title'] = 'Dashboard'
        return super().get_context_data(**kwargs)
