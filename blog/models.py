from django.db import models
from django.urls import reverse


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name}"

    

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    post_content = models.TextField()
    date = models.DateField()
    slug = models.SlugField(default="", null=False, db_index=True, blank=True)

    def get_absolute_url(self):
        return reverse("post-detail-page", args=[self.slug])
    
    def __str__(self) -> str:
        return f"{self.title}"
    