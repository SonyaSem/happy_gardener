# Generated by Django 3.2 on 2021-06-24 16:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Вид растения')),
            ],
            options={
                'verbose_name': 'Вид растения',
                'verbose_name_plural': 'Виды растений',
            },
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, unique=True, verbose_name='Название растения')),
                ('description', models.TextField(verbose_name='Описание растения')),
                ('date_of_plant', models.DateField(default=datetime.date.today, null=True, verbose_name='Дата посадки')),
                ('place_of_purchase', models.CharField(max_length=256, verbose_name='Место покупки')),
                ('date_of_purchase', models.DateField(default=datetime.date.today, null=True, verbose_name='Дата покупки')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Цена')),
                ('date_of_collect', models.DateField(default=datetime.date.today, null=True, verbose_name='Дата сбора')),
                ('date_of_last_water', models.DateField(default=datetime.date.today, null=True, verbose_name='Дата последнего полива')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plant', to='mainapp.category')),
            ],
            options={
                'verbose_name': 'Растение',
                'verbose_name_plural': 'Растения',
            },
        ),
    ]
