# Generated by Django 2.0 on 2018-11-24 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo2shareduser',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='photo2shareduser',
            name='user',
        ),
        migrations.DeleteModel(
            name='Photo2SharedUser',
        ),
    ]
