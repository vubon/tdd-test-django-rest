from django.db import models


# Create your models here.


class Contact(models.Model):
    """
    A contact Model
    Defines the attributes of a Contact Model
    """
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    age = models.IntegerField()
    bio = models.TextField(max_length=500, blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def person_name(self):
        return self.name + " owner of this mobile " + self.mobile

    def __repr__(self):
        return self.name + ' is added. '

