# Generated by Django 5.0.6 on 2024-05-17 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recipe', '0003_recipe_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_view_count',
            field=models.IntegerField(default=1),
        ),
    ]
