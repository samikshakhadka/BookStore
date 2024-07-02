from django.db import models
from django.conf import settings
from django.utils import timezone
from apps.book.models import Book

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('book', 'user')

    def __str__(self):
        return f'Review of {self.book.title} by {self.user.email}'
