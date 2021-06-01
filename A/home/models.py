from django.db import models


class Person(models.Model):
    name = models.CharField(max_length = 300)
    age = models.PositiveIntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name
