# Generated by Django 4.1 on 2022-09-13 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_alter_about_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('higher_edu_title', models.CharField(max_length=255)),
                ('higher_edu_description', models.TextField()),
                ('university_year', models.CharField(max_length=2083)),
                ('inter_edu_title', models.CharField(max_length=255)),
                ('inter_edu_description', models.TextField()),
                ('college_year', models.CharField(max_length=2083)),
                ('metric_edu_title', models.CharField(max_length=255)),
                ('metric_edu_description', models.TextField()),
                ('school_year', models.CharField(max_length=2083)),
            ],
        ),
    ]
