from kolibri.plugins import KolibriPluginBase

from . import settings


class DesktopUserAuth(KolibriPluginBase):
    translated_view_urls = "urls"
    settings_module = settings
