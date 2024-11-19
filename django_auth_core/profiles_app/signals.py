from django.dispatch import receiver
from djoser.signals import user_registered

from .models import Profile


@receiver(user_registered, dispatch_uid="create_profile") # декоратор к созданию пользователя
def create_profile(sender, user, request, **kwargs): # Создаёт профиль пользователя при регистрации

    data = request.data

    Profile.objects.create(
        user=user,
        name=data.get("name", ""),
        surname=data.get("surname", "")
    )
