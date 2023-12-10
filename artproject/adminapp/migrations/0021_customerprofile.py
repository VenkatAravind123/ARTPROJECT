# Generated by Django 4.2.5 on 2023-11-04 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0020_artistprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('name', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminapp.customer')),
            ],
        ),
    ]
