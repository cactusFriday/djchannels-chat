from django.db import models
from django.contrib.auth import get_user_model

USER = get_user_model()

class Message(models.Model):
    author = models.OneToOneField(USER, on_delete=models.CASCADE, related_name='author_message')
    text = models.TextField(max_length=256)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'MSG [{self.author.username}]:[{self.timestamp}]'

    def get_last_messages(self, number=10):
        return Message.objects.order_by('-timestamp').all()[:number]
