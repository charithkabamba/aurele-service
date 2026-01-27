from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Blog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blogs')
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)


    def __str__(self):
        return self.title
    
    # date format
    def published_at_formatted(self):
        return self.published_at.strftime('%Y-%m-%d %H:%M:%S')
    
    class Meta:
        ordering = ['-published_at']
    verbose_name = 'Blog'
    verbose_name_plural = 'Blogs'

