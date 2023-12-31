# Generated by Django 4.2.5 on 2023-10-06 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_alter_customer_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='gender',
            field=models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('Others', 'OTHERS')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='artist',
            name='phonenumber',
            field=models.CharField(default='', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('Others', 'OTHERS')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phonenumber',
            field=models.CharField(default='', max_length=20, unique=True),
        ),
    ]
