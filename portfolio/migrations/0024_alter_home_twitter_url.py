# Generated by Django 4.1 on 2022-11-23 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0023_alter_home_twitter_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="home",
            name="twitter_url",
            field=models.CharField(max_length=2083),
        ),
    ]
