# Generated by Django 2.2.9 on 2020-01-10 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20200110_0317'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='sort',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]