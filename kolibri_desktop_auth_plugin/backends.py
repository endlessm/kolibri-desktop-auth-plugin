import dbus

from .models import DaemonAuthUser


DBUS_ID = "org.learningequality.Kolibri.Daemon"
DBUS_PATH = "/" + DBUS_ID.replace(".", "/")
IFACE = "org.learningequality.Kolibri.Daemon.Private"


class TokenAuthBackend:
    def _get_user_details(self, token):
        bus = dbus.SessionBus()
        obj = bus.get_object(DBUS_ID, DBUS_PATH)
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

        uid = user_details["uid"]
        username = user_details["username"]
        admin = user_details["admin"]
        user = DaemonAuthUser.get_or_create(uid, username, admin)
        return user.user

    def get_user(self, user_id):
        try:
            return DaemonAuthUser.objects.get(user__pk=user_id).user
        except DaemonAuthUser.DoesNotExist:
            return None
