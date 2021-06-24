from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=250, verbose_name="Вид растения")


class Plant(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="plant")
    title = models.CharField(max_length=250, verbose_name="Название растения")
    description = models.TextField(verbose_name="Описание растения")
    place_of_purchase = models.CharField(max_length=250, verbose_name="Место покупки")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена")
