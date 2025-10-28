from django.contrib import admin
# import parler admin
from parler.admin import TranslatableAdmin
from .models import CatService, Service, AboutSection, Carousel

# Register your models here.
@admin.register(CatService)
class CatServiceAdmin(TranslatableAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('translations__name',)

@admin.register(Service)
class ServiceAdmin(TranslatableAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at')
    search_fields = ('translations__title', 'category__translations__name')

@admin.register(AboutSection)
class AboutSectionAdmin(TranslatableAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('translations__title',)
    
@admin.register(Carousel)
class CarouselAdmin(TranslatableAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('translations__title',)
