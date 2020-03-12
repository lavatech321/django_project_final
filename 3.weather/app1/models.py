from django.db import models

class CityModel(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return 'Name:{}'.format(self.name)

	class Meta:
		verbose_name_plural = 'cities'
# Create your models here.
