from django.contrib import admin
from .models import Post, Author

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}

admin.site.register(Post, PostAdmin)
admin.site.register(Author)