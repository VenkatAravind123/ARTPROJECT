# Generated by Django 4.2.5 on 2023-11-03 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0011_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('OilPaintings', 'OilPaintings'), ('PencilPaintings', 'PencilPaintings'), ('Glasspaintings', 'Glasspaintings'), ('WaterPaintings', 'WaterPaintings'), ('CarvedSculptures', 'CarvedSculptures'), ('AssembledSculptures', 'AssembledSculptures'), ('ReliefSculptures', 'ReliefSculptures')], max_length=100),
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/product/'),
        ),
    ]
