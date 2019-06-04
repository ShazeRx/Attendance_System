from django.contrib.auth.base_user import BaseUserManager


class TeacherManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self,username,password=None):
        user=self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,username,password):
        user=self.create_user(username,password=password)
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user