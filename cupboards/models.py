from django.db import models

# Create your models here.


class Material(models.Model):

    material_code = models.CharField(max_length=3)
    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)
    price_per_m2 = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name


class Type(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Cupboard(models.Model):

    design_id = models.CharField(max_length=5)
    type = models.ForeignKey('Type', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    material = models.ForeignKey('Material', null=True, blank=False,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    design_surcharge = models.DecimalField(max_digits=6, decimal_places=2)
    exampleprice = models.DecimalField(max_digits=6, decimal_places=2)
    main_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name 


class GalleryImage(models.Model):
    cupboard = models.ForeignKey(Cupboard, on_delete=models.CASCADE)
    file_name = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.file_name.path

class SavedCupboard(models.Model):

    user = models.CharField(max_length=254, null=True, blank=False)
    cupboard = models.ForeignKey(Cupboard, on_delete=models.CASCADE, null=True, blank=False)
    height = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=False)
    width = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=False)
    depth = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=False)
    shelves = models.IntegerField(null=True, blank=False)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=False)
    code = models.CharField(max_length=254, null=True, blank=False)

    def __str__(self):
        return self.name 

