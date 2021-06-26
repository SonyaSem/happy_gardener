from django.db import models
from datetime import date

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=250, verbose_name="Вид растения")

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Вид растения"
        verbose_name_plural = "Виды растений"


class Plant(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="plant")
    title = models.CharField(max_length=256, verbose_name="Название растения", unique=True)
    description = models.TextField(verbose_name="Описание растения")
    date_of_plant = models.DateField(default=date.today, verbose_name="Дата посадки", null=True)
    place_of_purchase = models.CharField(max_length=256, verbose_name="Место покупки")
    date_of_purchase = models.DateField(default=date.today, verbose_name="Дата покупки", null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена")
    date_of_collect = models.DateField(default=date.today, verbose_name="Дата сбора", null=True)
    date_of_last_water = models.DateField(default=date.today, verbose_name="Дата последнего полива", null=True)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('plant_detail_view', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Растение"
        verbose_name_plural = "Растения"


class Photo (models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    comment = models.TextField()

    def __str__(self):
        return str(self.comment)
