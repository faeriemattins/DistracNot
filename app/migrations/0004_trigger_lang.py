# Generated by Django 2.2.8 on 2021-05-02 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210502_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='trigger',
            name='lang',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
