from django.db import models
import uuid
# Create your models here.

class Basemodel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


