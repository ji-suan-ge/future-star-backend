# Generated by Django 2.2.9 on 2020-01-01 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accept_absence', models.IntegerField(choices=[(0, '接受'), (1, '拒绝')])),
                ('reason_application', models.TextField()),
                ('contribution_for_us', models.TextField()),
                ('way', models.CharField(choices=[('wx', '微信朋友圈'), ('friend', '朋友推荐'), ('Public', '未来之星公众号：EdStars未来同学会'), ('web', '好未来官网'), ('media', '媒体报道'), ('others', '其他')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('website', models.CharField(max_length=30)),
                ('wx_public', models.CharField(max_length=30)),
                ('create_time', models.DateField()),
                ('city', models.CharField(max_length=30)),
                ('number_employee', models.IntegerField()),
                ('position', models.CharField(max_length=30)),
                ('introduction', models.TextField()),
                ('company_data', models.TextField()),
                ('income_scale', models.CharField(max_length=30)),
                ('financing_situation', models.CharField(choices=[('N', '尚未获得融资'), ('seed/angel', '已完成种子/天使融资'), ('pre-A', '已完成pre-A轮融资'), ('A', '已完成A轮融资'), ('refuse', '不方便透露'), ('others', '其他')], max_length=30)),
                ('value_of_assessment', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fraction', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('gender', models.IntegerField(choices=[(0, '男'), (1, '女')], default=0)),
                ('birthday', models.DateField()),
                ('phone_number', models.CharField(max_length=11)),
                ('wx', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('education', models.CharField(choices=[('PhD', '博士'), ('MBA', '硕士'), ('Bachelor', '本科'), ('College', '专科'), ('Others', '其他')], max_length=30)),
                ('school', models.CharField(max_length=30)),
                ('previous_company', models.CharField(max_length=30)),
                ('previous_position', models.CharField(max_length=30)),
                ('state', models.IntegerField(choices=[(0, '不再是校友'), (1, '还未毕业的校友'), (2, '校友')])),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Company')),
            ],
        ),
        migrations.CreateModel(
            name='RecommendationPeople',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('company', models.CharField(max_length=30)),
                ('position', models.CharField(max_length=30)),
                ('information', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.ApplicationInformation')),
            ],
        ),
    ]
