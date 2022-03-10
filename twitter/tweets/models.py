from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=24)

    def __str__(self):
        return self.name


class Tweet(models.Model):
    text = models.CharField(max_length=224, null=False, blank=False)
    likes = models.IntegerField(default=0)
    create_date = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.text[:45]
