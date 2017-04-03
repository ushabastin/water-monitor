import datetime
from django.db import models
from django.utils import timezone


class Nodename(models.Model):
    title = models.CharField(max_length=200, default='Node')
    text = models.TextField()
    created_date = models.DateTimeField('Start Date',
            default=timezone.now)
    published_date = models.DateTimeField('Last updated on', default=timezone.now)

    def was_published_recently(self):
        return self.published_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'published_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Modified recently?'

    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.title


class Sensordata(models.Model):
    node_id = models.ForeignKey(Nodename)
    param = models.CharField(max_length=50)
    unit = models.CharField(max_length=20, blank=True, null=True)
    value = models.CharField(max_length=5)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.param
