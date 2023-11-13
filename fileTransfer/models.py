import uuid
from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.

class SharedFile(models.Model):
    title = models.CharField(max_length=100)
    access_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    shareable_link = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, )
    expiration_time = models.DateTimeField(null=True, blank=True)
    file = models.FileField(
        upload_to='',
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'txt'])]
    )
    def __str__(self):
        return self.title