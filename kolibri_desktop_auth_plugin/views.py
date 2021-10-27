from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views import View
from kolibri.dist.django.core.urlresolvers import reverse


class LoginView(View):
    def get(self, request, token):
        user = authenticate(token=token)
        if not user:
            return redirect(reverse("kolibri:core:redirect_user"))

        login(request, user)

        next_url = request.GET.get("next")
        if next_url:
            return redirect(next_url)

        return redirect("/")
