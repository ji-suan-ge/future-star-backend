# Generated by Django 2.2.9 on 2020-01-09 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20200109_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birthday',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='city',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.Company'),
        ),
        migrations.AlterField(
            model_name='student',
            name='education',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.IntegerField(choices=[(0, '男'), (1, '女')], default=0, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone_number',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='previous_company',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='previous_position',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='profession',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='school',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='state',
            field=models.IntegerField(choices=[(0, '不再是校友'), (1, '还未毕业的校友'), (2, '校友')], default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='wx',
            field=models.CharField(max_length=30, null=True),
        ),
    ]