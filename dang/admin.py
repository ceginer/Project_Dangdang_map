from django.contrib import admin
from .models import User, Post, Cafe, Place, Accomodation, Medical, Location

# Register your models here.
@admin.register(User)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Cafe)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Place)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Accomodation)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Medical)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Location)
class PostAdmin(admin.ModelAdmin):
    pass