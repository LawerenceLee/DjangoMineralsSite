from django.db import models


class Mineral(models.Model):
    name = models.CharField(max_length=200, blank=True, null=False)
    image_filename = models.CharField(max_length=200, blank=True, null=False)
    image_caption = models.CharField(max_length=200, blank=True, null=False)
    formula = models.CharField(max_length=200, blank=True, null=False)
    color = models.CharField(max_length=200, blank=True, null=False)
    cleavage = models.CharField(max_length=200, blank=True, null=False)
    streak = models.CharField(max_length=200, blank=True, null=False)
    luster = models.CharField(max_length=200, blank=True, null=False)
    mohs_scale_hardness = models.CharField(max_length=200, blank=True, null=False)
    optical_properties = models.CharField(max_length=200, blank=True, null=False)
    category = models.CharField(max_length=200, blank=True, null=False)
    crystal_habit = models.CharField(max_length=200, blank=True, null=False)
    crystal_system = models.CharField(max_length=200, blank=True, null=False)
    crystal_symmetry = models.CharField(max_length=200, blank=True, null=False)
    group = models.CharField(max_length=200, blank=True, null=False)
    strunz_classification = models.CharField(max_length=200, blank=True, null=False)
    refractive_index = models.CharField(max_length=200, blank=True, null=False)
    unit_cell = models.CharField(max_length=200, blank=True, null=False)
    specific_gravity = models.CharField(max_length=200, blank=True, null=False)
    diaphaneity = models.CharField(max_length=200, blank=True, null=False)
