from gi.repository import Gio

from .models import DesktopUser


DBUS_ID = "org.learningequality.Kolibri.Daemon"
DBUS_PATH = "/" + DBUS_ID.replace(".", "/")
IFACE = DBUS_ID + ".Private"


class TokenAuthBackend:
    def _get_user_details(self, token):
        bus = Gio.bus_get_sync(Gio.BusType.SESSION, None)
        proxy = Gio.DBusProxy.new_sync(bus, 0, None,
                                       DBUS_ID,
                                       DBUS_PATH,
                                       IFACE,
                                       None)

        try:
            details = proxy.GetUserDetails("(s)", token)
        except Exception:
            return None

        return details

    def authenticate(self, request, token=None, **kwargs):
        user_details = self._get_user_details(token)
        if not user_details:
            return None

        user = DesktopUser.objects.get_or_create(**user_details)
        return user.user

    def get_user(self, user_id):
        try:
            return DesktopUser.objects.get(user__pk=user_id).user
        except DesktopUser.DoesNotExist:
            return None
