from django.db import models

# Create your models here.
class Article(models.Model):
    class Meta():
        db_table = 'article'
    article_title = models.CharField(max_length=200)
    article_text = models.TextField()
    article_image = models.ImageField()

