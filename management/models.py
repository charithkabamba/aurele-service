from django.db import models
# import parler
from parler.models import TranslatableModel, TranslatedFields
import uuid

# Create your models here.

class CatService(TranslatableModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    translations = TranslatedFields(
        name = models.CharField(max_length=200)
    )
    icon = models.CharField(max_length=200, blank=True, null=True)  # icon class for font-awesome or similar
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True) or "Unnamed Category"
    
class Service(TranslatableModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    translations = TranslatedFields(
        title = models.CharField(max_length=200),
        description = models.TextField()
    )
    category = models.ForeignKey(CatService, on_delete=models.CASCADE, related_name='services')
    icon = models.CharField(max_length=200, blank=True, null=True)  # icon class for font-awesome or similar
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image_url = models.URLField(blank=True, null=True)  # URL for the service image
    image_file = models.ImageField(upload_to='services/', blank=True, null=True)  # Uploaded image file

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True) or "Unnamed Service"
    
    # about page
class AboutSection(TranslatableModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    translations = TranslatedFields(
        title = models.CharField(max_length=200),
        content = models.TextField(),
        description = models.TextField(blank=True, null=True)
    )
    icon = models.CharField(max_length=200, blank=True, null=True)  # icon class for font-awesome or similar
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    picture = models.ImageField(upload_to='about/pictures/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True) or "Unnamed About Section"

class Carousel(TranslatableModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    translations = TranslatedFields(
        title = models.CharField(max_length=200),
        subtitle = models.CharField(max_length=200, blank=True, null=True),
        description = models.TextField(blank=True, null=True)
    )
    image = models.ImageField(upload_to='carousel/')
    link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.safe_translation_getter('title', any_language=True) or "Unnamed Carousel Item"
    
class Testimonial(TranslatableModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    translations = TranslatedFields(
        client_name = models.CharField(max_length=200),
        content = models.TextField(),
        position = models.CharField(max_length=200, blank=True, null=True)  # e.g., CEO, Manager
    )
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.safe_translation_getter('client_name', any_language=True) or "Unnamed Testimonial"
    
class TeamMember(TranslatableModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    translations = TranslatedFields(
        name = models.CharField(max_length=200),
        role = models.CharField(max_length=200),
        bio = models.TextField(blank=True, null=True)
    )
    image = models.ImageField(upload_to='team/', blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.safe_translation_getter('name', any_language=True) or "Unnamed Team Member"
    
class FAQ(TranslatableModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    translations = TranslatedFields(
        question = models.CharField(max_length=300),
        answer = models.TextField()
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.safe_translation_getter('question', any_language=True) or "Unnamed FAQ"
    
class ContactMessage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
    
class Partner(TranslatableModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    translations = TranslatedFields(
        name = models.CharField(max_length=200),
        website = models.URLField(blank=True, null=True)
    )
    logo = models.ImageField(upload_to='partners/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True) or "Unnamed Partner"
    
