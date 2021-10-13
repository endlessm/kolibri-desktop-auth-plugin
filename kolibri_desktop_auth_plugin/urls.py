from django.conf.urls import url

from .views import LoginView


urlpatterns = [
    url(r"login/(?P<token>[\w\-]+)", LoginView.as_view(), name="login"),
]
