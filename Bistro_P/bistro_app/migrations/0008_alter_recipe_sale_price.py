# Generated by Django 4.0.6 on 2022-07-11 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bistro_app', '0007_alter_ingredient_id_alter_menu_id_alter_menuitem_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='sale_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
