# Generated by Django 2.2.12 on 2021-10-09 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='place',
            field=models.CharField(default='place', max_length=50),
            preserve_default=False,
        ),
    ]
