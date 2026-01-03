from django.db import models
from django.urls import reverse


class Post(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255, unique=True)
	image = models.ImageField(upload_to='blog/', blank=True, null=True)
	summary = models.TextField(blank=True)
	content = models.TextField()
	category = models.CharField(max_length=100, blank=True)
	published_at = models.DateTimeField(blank=True, null=True)
	is_published = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-published_at', '-created_at']
		verbose_name = 'Post'
		verbose_name_plural = 'Posts'

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:detail', kwargs={'slug': self.slug})

