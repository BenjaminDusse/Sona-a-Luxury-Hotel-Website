# Generated by Django 3.2.9 on 2021-12-09 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('res_system', '0002_rename_size_in_ft_room_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
