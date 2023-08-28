from gi.repository import Gio

from .config import DBUS_NAME
from .models import DesktopUser


try:
    import kolibri_app.config
except ImportError:
    DBUS_ID = DBUS_NAME + ".Daemon"
    DBUS_PATH = "/" + DBUS_ID.replace(".", "/") + "/Private"
else:
    DBUS_ID = kolibri_app.config.DAEMON_APPLICATION_ID
    DBUS_PATH = kolibri_app.config.DAEMON_PRIVATE_OBJECT_PATH

IFACE = DBUS_ID + ".Private"


class TokenAuthBackend:
    def _get_user_details(self, token):
        bus = Gio.bus_get_sync(Gio.BusType.SESSION, None)
        proxy = Gio.DBusProxy.new_sync(
            bus, 0, None, DBUS_ID, DBUS_PATH, IFACE, None
        )

        try:
            details = proxy.CheckLoginToken("(s)", token)
        except Exception:
            return None

        return details

    def authenticate(self, request, token=None, **kwargs):
        # This method is being tried automatically by Django, but it's
        # supposed to be called only from the view:
        if token is None:
            return None

        user_details = self._get_user_details(token)
        if not user_details:
            return None

        if "user_id" not in user_details:
            return None

        user = DesktopUser.objects.get_or_create(**user_details)
        return user.user

    def get_user(self, user_id):
        try:
            return DesktopUser.objects.get(user__pk=user_id).user
        except DesktopUser.DoesNotExist:
            return None
