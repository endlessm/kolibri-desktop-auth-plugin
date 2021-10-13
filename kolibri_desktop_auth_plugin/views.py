from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.views import View


class LoginView(View):
    def get(self, request, token):
        user = authenticate(token=token)
        if not user:
            return HttpResponseRedirect("/auth")

        login(request, user)

        next_url = request.GET.get("next")
        if next_url:
            return HttpResponseRedirect(next_url)

        return HttpResponseRedirect("/")
