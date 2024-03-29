from django.db import models
from datetime import datetime
# Create your models here.
class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_content = models.TextField()
    blog_published = models.DateTimeField('Date Published', default=datetime.now)

    def __str__(self):
        return self.blog_title