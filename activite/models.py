from django.db import models
from django.urls import reverse

class Project(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255, unique=True)
	image = models.ImageField(upload_to='projects/', blank=True, null=True)
	excerpt = models.TextField(blank=True)
	content = models.TextField(blank=True)
	category = models.CharField(max_length=100, blank=True)
	published_at = models.DateTimeField(blank=True, null=True)
	is_published = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-published_at', '-created_at']
		verbose_name = 'Project'
		verbose_name_plural = 'Projects'

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('activite:project_detail', kwargs={'slug': self.slug})

