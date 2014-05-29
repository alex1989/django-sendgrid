from django.db import models
from django.contrib.contenttypes.generic import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _


import uuid


class Email(models.Model):
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    email = models.CharField(_('addressee'), max_length=512)
    event = models.CharField(_('event type'), max_length=32)
    timestamp = models.DateTimeField(_('timestamp'))
    uuid = models.CharField(_('reference UUID'), max_length=64, default=lambda: str(uuid.uuid4()))

    def __unicode__(self):
        return '%s: %s' % (self.email, self.event)
