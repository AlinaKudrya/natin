# Generated by Django 3.1.1 on 2020-11-27 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website_Natin_Travel', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='featuredtours',
            options={'verbose_name': 'Избранный тур', 'verbose_name_plural': 'Избранные туры'},
        ),
        migrations.AddField(
            model_name='applications',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата заявки'),
        ),
    ]