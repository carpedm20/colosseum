from django.db import models

from account.models import Account

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created_at  = models.DateTimeField(auto_now_add=True)

    creator = models.ForeignKey(Account, null=True)

    def __unicode__(self):
        return self.name
