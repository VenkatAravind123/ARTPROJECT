# Generated by Django 4.2.5 on 2023-10-08 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0004_alter_artist_gender_alter_artist_phonenumber_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='name',
            new_name='username',
        ),
        migrations.AddField(
            model_name='artist',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
    ]
