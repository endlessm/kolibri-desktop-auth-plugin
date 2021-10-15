import dbus

from .models import DaemonAuthUser


DBUS_ID = "org.learningequality.Kolibri.Daemon"
DBUS_PATH = "/" + DBUS_ID.replace(".", "/")
IFACE = DBUS_ID + ".Private"


class TokenAuthBackend:
    def _get_user_details(self, token):
        bus = dbus.SessionBus()
        try:
            obj = bus.get_object(DBUS_ID, DBUS_PATH)
        except dbus.exceptions.DBusException:
            return None

        iface = dbus.Interface(obj, IFACE)
        try:
            variant = iface.GetUserDetails(token)
        except Exception:
            return None

        return variant

    def authenticate(self, request, token=None, **kwargs):
        user_details = self._get_user_details(token)
        if not user_details:
            return None

        user = DaemonAuthUser.objects.get_or_create(**user_details)
        return user.user

    def get_user(self, user_id):
        try:
            return DaemonAuthUser.objects.get(user__pk=user_id).user
        except DaemonAuthUser.DoesNotExist:
            return None
