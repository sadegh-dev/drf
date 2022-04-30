from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    
    def __str__(self):
        return self.name


class Author(models.Model):
    name =      models.CharField(max_length=150)
    email =     models.EmailField(max_length=254, unique=True)
    bio =       models.TextField(1000, null=True, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    category =      models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    authors =       models.ManyToManyField(Author)    
    name =          models.CharField(max_length=150)
    description =   models.TextField(max_length=1000, null=True, blank=True)
    pages =         models.PositiveIntegerField()
    is_active =     models.BooleanField(default=True)
    created =       models.DateTimeField(auto_now_add=True)
    updated =       models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.category.name}'

