from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'cities'

    def __str__(self):
        return self.name

class Advert(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    views = models.IntegerField(default=0)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = 'adverts'

    def __str__(self):
        return self.title