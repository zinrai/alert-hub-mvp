from django.db import models
from django.utils.translation import gettext_lazy as _

class Alert(models.Model):
    URGENCY_CHOICES = [
        ('LOW', _('低')),
        ('MEDIUM', _('中')),
        ('HIGH', _('高')),
    ]
    STATUS_CHOICES = [
        ('OPEN', _('未対応')),
        ('IN_PROGRESS', _('対応中')),
        ('CLOSED', _('完了')),
        ('ON_HOLD', _('保留')),
    ]

    subject = models.CharField(max_length=200)
    body = models.TextField()
    identifier = models.CharField(max_length=50, unique=True)
    urgency = models.CharField(max_length=10, choices=URGENCY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='OPEN')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject
