from django.db import models

from django.urls import reverse


class Project(models.Model):
	"""Database model for storing projects"""
	title = models.CharField(max_length=50)
	description = models.CharField(max_length=250)
	image = models.ImageField(upload_to='resume/images/')
	url = models.URLField(blank=True)

	def __str__(self):
		"""Return model as string"""
		return self.title

	def get_absolute_url(self):
		"""Return project id"""
		return reverse('detail', kwargs={
			'project_id' : self.id
		})