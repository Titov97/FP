# Generated by Django 4.0.4 on 2022-07-20 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bistro_app', '0012_salesmenu_category_alter_menuitem_menu_delete_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesmenu',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bistro_app.category'),
            preserve_default=False,
        ),
    ]
