# Generated by Django 2.2.9 on 2019-12-28 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.IntegerField()),
                ('content_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.IntegerField()),
                ('teacher_id', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
                ('introduction', models.TextField()),
                ('location', models.CharField(max_length=30)),
                ('begin_time', models.DateField()),
                ('end_time', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_id', models.IntegerField()),
                ('type', models.CharField(choices=[(0, '文本'), (1, 'PPT'), (2, '视频')], max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('url', models.CharField(max_length=30)),
                ('word', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('avatar', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=30)),
                ('introduction', models.TextField()),
                ('contact_way', models.CharField(max_length=30)),
            ],
        ),
    ]