from .models import DaemonAuthUser


class TokenAuthBackend:
    def _get_user_details(self, token):
        # TODO: call the real kolibri-daemon to GetUserDetails
        return {
            "username": "eosuser",
            "uid": 1000,
            "gid": 1000,
            "groups": [],
            "admin": True,
        }

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
