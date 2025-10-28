from django.db import models
# import user
from django.contrib.auth.models import User

# Create your models here.
import uuid
from parler.models import TranslatableModel, TranslatedFields

class userProfession(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='professions')
    profession_name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.profession_name}"
    
class Project(TranslatableModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_profession = models.ForeignKey(userProfession, on_delete=models.CASCADE, related_name='projects')
    translations = TranslatedFields(
        title = models.CharField(max_length=50),
        subtitle = models.CharField(max_length=50, blank=True, null=True),
        description = models.TextField()
    )
    image_url = models.URLField(blank=True, null=True)  # URL for the project image
    image_file = models.ImageField(upload_to='projects/', blank=True, null=True)  # Uploaded image file
    project_link = models.URLField(blank=True, null=True)  # Link to the project (if applicable)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True) or "Unnamed Project"
    
class Skill(TranslatableModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_profession = models.ForeignKey(userProfession, on_delete=models.CASCADE, related_name='skills')
    translations = TranslatedFields(
        name = models.CharField(max_length=100)
    )
    proficiency_level = models.CharField(max_length=100, blank=True, null=True)  # e.g., Beginner, Intermediate, Expert
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True) or "Unnamed Skill"
    
class Experience(TranslatableModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_profession = models.ForeignKey(userProfession, on_delete=models.CASCADE, related_name='experiences')
    translations = TranslatedFields(
        title = models.CharField(max_length=200),
        company = models.CharField(max_length=200),
        description = models.TextField(blank=True, null=True)
    )
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)  # null if currently working
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True) or "Unnamed Experience"
    
class Education(TranslatableModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_profession = models.ForeignKey(userProfession, on_delete=models.CASCADE, related_name='educations')
    translations = TranslatedFields(
        institution = models.CharField(max_length=200),
        degree = models.CharField(max_length=200),
        field_of_study = models.CharField(max_length=200, blank=True, null=True),
        description = models.TextField(blank=True, null=True)
    )
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)  # null if currently studying
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.safe_translation_getter('institution', any_language=True) or "Unnamed Education"
    
class Certification(TranslatableModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_profession = models.ForeignKey(userProfession, on_delete=models.CASCADE, related_name='certifications')
    translations = TranslatedFields(
        name = models.CharField(max_length=200),
        issuing_organization = models.CharField(max_length=200),
        description = models.TextField(blank=True, null=True)
    )
    issue_date = models.DateField()
    expiration_date = models.DateField(blank=True, null=True)  # null if does not expire
    credential_id = models.CharField(max_length=200, blank=True, null=True)
    credential_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True) or "Unnamed Certification"
    
class Domain(TranslatableModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_profession = models.ForeignKey(userProfession, on_delete=models.CASCADE, related_name='domains')
    translations = TranslatedFields(
        name = models.CharField(max_length=200),
        description = models.TextField(blank=True, null=True)
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True) or "Unnamed Domain"
    
class Language(TranslatableModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_profession = models.ForeignKey(userProfession, on_delete=models.CASCADE, related_name='languages')
    translations = TranslatedFields(
        name = models.CharField(max_length=100),
        proficiency_level = models.CharField(max_length=100, blank=True, null=True)  # e.g., Basic, Conversational, Fluent, Native

    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True) or "Unnamed Language"
    


