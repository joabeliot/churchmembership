from django.db import models
import uuid

class Identity(models.Model):

    class Meta:
        verbose_name_plural = "identities"

    email = models.EmailField(unique=True)
    uid = models.UUIDField(default = uuid.uuid4, unique=True)
    fullName = models.CharField(max_length=60)
    passwordHash = models.CharField()
    hashSalt = models.CharField()
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField(null=True)
    lastLoginAt = models.DateTimeField()