from django.db import models


class SubscriberManager(models.Manager):
    def get_active_subscribers(self):
        return self.filter(status="active").values('id', 'email', 'first_name')

    def get_inactive_subscribers(self):
        return self.filter(status="inactive").values('id', 'email', 'first_name')
    pass


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    status = models.CharField(max_length=20,default='active')
    objects = SubscriberManager()

    def deactivate(self):
        self.status = 'inactive'
        self.save()

