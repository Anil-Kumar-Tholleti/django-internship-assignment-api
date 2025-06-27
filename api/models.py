
from django.db import models
from django.contrib.auth.models import User

class TelegramUser(models.Model):
    telegram_username = models.CharField(max_length=255, unique=True)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.telegram_username
