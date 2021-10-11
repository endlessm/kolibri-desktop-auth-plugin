from django.views import View
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth import authenticate, login


class LoginView(View):
    def get(self, request, token):
        user = authenticate(token)
        if not user:
            return HttpResponseForbidden()

        login(request, user)

        next_url = request.GET.get("next")
        if next_url:
            return HttpResponseRedirect(next_url)

        return HttpResponseRedirect("/")
