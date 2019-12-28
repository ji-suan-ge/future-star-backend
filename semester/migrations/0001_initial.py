# Generated by Django 2.2.9 on 2019-12-28 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period_semester', models.IntegerField()),
                ('subject', models.TextField()),
                ('introduction', models.TextField()),
                ('state', models.IntegerField(choices=[(0, '正在进行'), (1, '已结束')], default=0)),
            ],
        ),
    ]
