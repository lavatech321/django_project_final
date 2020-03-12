from django.db import models

class TodoModel(models.Model):
	text = models.CharField(max_length=40)
	complete = models.BooleanField(default=False)

	def __str__(self):
		return 'ID:{} Name:{} Complete:{}'.format(self.id,self.text,self.complete)
# Create your models here.
