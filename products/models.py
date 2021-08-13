from django.db import models


class Material(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=False, blank=False)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Angle(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=False, blank=False)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Level(models.Model):

    name = models.CharField(max_length=254, null=False, blank=False)
    friendly_name = models.CharField(max_length=254, null=False, blank=False)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):

    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    material = models.ForeignKey(
        'Material', null=True, blank=True, on_delete=models.SET_NULL)
    angle = models.ForeignKey(
        'Angle', null=True, blank=True, on_delete=models.SET_NULL)
    level = models.ForeignKey(
        'Level', null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    image_1 = models.ImageField(null=True, blank=True)
    image_2 = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=2014, null=True, blank=True)
    unavailable = models.BooleanField(default=False)

    def __str__(self):
        return self.name
