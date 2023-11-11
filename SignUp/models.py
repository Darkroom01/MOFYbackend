from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, birthdate, gen, nickname, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            birthdate=birthdate,
            gen=gen,
            nickname=nickname,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, birthdate, gen, nickname, password=None):
        user = self.create_user(
            email,
            password=password,
            name=name,
            birthdate=birthdate,
            gen=gen,
            nickname=nickname,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=10)
    birthdate = models.DateField()
    gen = models.BooleanField(default=True)
    nickname = models.CharField(max_length=20)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'user'

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'birthdate', 'gen', 'nickname']

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
