from kolibri.plugins import KolibriPluginBase

from . import settings


class DaemonAuth(KolibriPluginBase):
    translated_view_urls = "urls"
    settings_module = settings

    @property
    def url_slug(self):
        return r"daemon-auth/"
