# Generated by Django 3.2.5 on 2021-11-26 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_material_is_sustainable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
    ]
