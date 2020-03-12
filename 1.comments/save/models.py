from django.db import models
from django.utils import timezone
# Create your models here.

class CommentModel(models.Model):
	name = models.CharField(max_length=30)
	comment = models.TextField()
	date_added = models.DateTimeField(default=timezone.now , blank=True)

	def __str__(self):
		return 'Name:{} and Date:{}'.format(self.name,self.date_added)
		
# Create your models here.
