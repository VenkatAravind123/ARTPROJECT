# Generated by Django 4.2.5 on 2023-11-03 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0012_alter_category_name_alter_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('OilPaintings', 'OilPaintings'), ('PencilPaintings', 'PencilPaintings'), ('Glasspaintings', 'Glasspaintings'), ('WaterPaintings', 'WaterPaintings'), ('CarvedSculptures', 'CarvedSculptures'), ('AssembledSculptures', 'AssembledSculptures'), ('ReliefSculptures', 'ReliefSculptures'), ('ModeledSculptures', 'ModeledSculptures')], max_length=100),
        ),
    ]
