from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
    text = models.TextField('Article text')

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.CharField(max_length=70)
    text = models.TextField('Comment text')

    def __str__(self):
        return "{} says '{}'".format(self.author, self.text)

