from django.db import models


class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=64)
    nickname = models.CharField(max_length=124, unique=True, default=login)

    def __str__(self):
        return f'nickname - {self.nickname}, id - {self.id}, password - {self.password}'


class Publication(models.Model):
    publication_date = models.DateTimeField('published', auto_now=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    media = models.ImageField(upload_to='media/', null=False, blank=True)
    comments = models.CharField(max_length=260, blank=True)

    def __str__(self):
        return f'comment by {self.author} on {self.publication_date}'
