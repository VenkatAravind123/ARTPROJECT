# Generated by Django 4.2.5 on 2023-11-04 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0018_alter_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='category',
            field=models.CharField(choices=[('Painter', 'Painter'), ('Sculptur', 'Sculpture')], max_length=25),
        ),
    ]