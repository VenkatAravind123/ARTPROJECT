# Generated by Django 4.2.5 on 2023-11-03 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0010_category_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Paintings', 'Paintings'), ('Sculptures', 'Sculptures')], max_length=100),
        ),
    ]
