from django.db import models

class Car(models.Model):
    title = models.CharField(max_length=40) # название машинок
    content = models.TextField()
    costs = models.IntegerField()
    create = models.IntegerField(default=2010)

    def __str__(self):
        return self.title
