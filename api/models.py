from datetime import datetime
import uuid
from django.db import models

# Create your models here.
class BaseMeta(models.Model):
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        abstract = True

class Post(BaseMeta):
    title = models.CharField(max_length=255, null=False)
    content = models.CharField(max_length=2000, null=False)
    image = models.ImageField()