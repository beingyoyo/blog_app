from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_content = models.TextField()
    blog_published = models.DateTimeField('Date Published')

    def __str__(self):
        return self.blog_title