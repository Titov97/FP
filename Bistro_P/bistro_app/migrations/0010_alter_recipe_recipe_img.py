# Generated by Django 4.0.4 on 2022-07-18 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bistro_app', '0009_recipe_recipe_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_img',
            field=models.ImageField(default='media/default.jpg', upload_to='media'),
        ),
    ]
