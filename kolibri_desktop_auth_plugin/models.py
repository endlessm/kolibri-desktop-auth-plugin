from django.db import models
from kolibri.core.auth.models import FacilityUser


class DesktopUserManager(models.Manager):
    def get_or_create(
        self,
        user_id=None,
        user_name=None,
        full_name=None,
        is_admin=False,
        **kwargs,
    ):
        try:
            user = DesktopUser.objects.get(uid=user_id)
        except DesktopUser.DoesNotExist:
            user = DesktopUser.create_user(
                user_id, user_name, full_name, is_admin
            )

        return user


class DesktopUser(models.Model):
    uid = models.CharField("uid", max_length=10, primary_key=True)
    user = models.ForeignKey(FacilityUser, on_delete=models.CASCADE)

    objects = DesktopUserManager()

    @classmethod
    def create_user(cls, uid, user_name, full_name=None, is_admin=False):
        create_user = FacilityUser.objects.create_user
        if is_admin:
            create_user = FacilityUser.objects.create_superuser

        # Using a different username if this is taken
        uname = user_name
        n = 0
        while FacilityUser.objects.filter(username=uname).exists():
            n += 1
            uname = "{}_{}".format(user_name, n)

        create_user(username=uname, password="NOT_SPECIFIED")

        kolibri_user = FacilityUser.objects.get(username=uname)
        kolibri_user.set_unusable_password()
        kolibri_user.gender = "NOT_SPECIFIED"
        kolibri_user.birth_year = "NOT_SPECIFIED"
        kolibri_user.full_name = full_name
        kolibri_user.save()

        user = cls(uid=uid, user=kolibri_user)
        user.save()

        return user

    def __str__(self):
        return '"{username}" ({uid})'.format(
            username=self.user.username, uid=self.uid
        )
