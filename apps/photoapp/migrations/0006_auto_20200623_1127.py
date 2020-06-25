# Generated by Django 2.0.5 on 2020-06-23 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoapp', '0005_photoposition_photo_with_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='position',
        ),
        migrations.AddField(
            model_name='photo',
            name='position',
            field=models.ForeignKey(blank=True, null=True, on_delete=True, to='photoapp.PhotoPosition'),
        ),
        migrations.RemoveField(
            model_name='photoposition',
            name='photo_with_position',
        ),
        migrations.AddField(
            model_name='photoposition',
            name='photo_with_position',
            field=models.ForeignKey(blank=True, null=True, on_delete=True, to='photoapp.Photo'),
        ),
    ]