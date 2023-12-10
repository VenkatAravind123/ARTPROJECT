# Generated by Django 4.2.5 on 2023-12-07 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0026_rename_phonenumber_artistprofile_phonenumber1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistprofile',
            name='phonenumber1',
            field=models.CharField(default='000', max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='customerprofile',
            name='phonenumber2',
            field=models.CharField(default='000', max_length=20, null=True, unique=True),
        ),
    ]