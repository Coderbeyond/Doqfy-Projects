from django.db import models
import uuid

class TextSnippet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.TextField()
    secret_key = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.id)
