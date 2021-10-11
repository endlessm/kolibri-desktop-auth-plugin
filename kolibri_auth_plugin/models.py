from django.db import models

from kolibri.core.auth.models import FacilityUser


class DaemonAuthUser(models.Model):
    uid = models.CharField("uid", max_length=10, primary_key=True)
    user = models.ForeignKey(FacilityUser, on_delete=models.CASCADE)

    @classmethod
    def get_or_create(cls, uid, username):
        try:
            user = cls.objects.get(uid=uid)
        except cls.DoesNotExist:
            # TODO: call create_superuser for admins
            # TODO: Use a different username if this is taken
            kolibri_user = FacilityUser.objects.create_user(
                username=username,
                password="not set",
            )
            kolibri_user.set_unusable_password()
            user = cls(uid=uid, user=kolibri_user)
            user.save()

        return user

    def __str__(self):
        return '"{username}" ({uid})'.format(
            username=self.user.username, uid=self.uid
        )
