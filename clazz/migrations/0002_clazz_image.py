# Generated by Django 2.2.9 on 2020-01-10 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clazz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clazz',
            name='image',
            field=models.CharField(default='https://i.loli.net/2020/01/10/QD97zMkbIs1hw4d.png', max_length=1000),
        ),
    ]