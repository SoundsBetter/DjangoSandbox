from django.db import models
from django.db.models import UniqueConstraint


class Consumer(models.Model):
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(
        max_length=3, choices=GENDER_CHOICES, blank=True, null=True
    )

    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ServiceProvider(models.Model):
    company_name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    service_description = models.TextField(blank=True, null=True)
    registered_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ConsumerServiceProvider(models.Model):
    consumer = models.ForeignKey(
        "Consumer", on_delete=models.CASCADE, related_name="service_providers"
    )
    service_provider = models.ForeignKey(
        "ServiceProvider", on_delete=models.CASCADE, related_name="consumers"
    )
    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=("consumer", "service_provider"),
                name="consumer_service_provider",
            )
        ]
