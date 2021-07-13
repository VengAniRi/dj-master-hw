from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.TextField(unique=True)
    price = models.IntegerField()
    image = models.TextField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)
