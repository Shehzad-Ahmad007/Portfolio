# Generated by Django 4.1.3 on 2022-11-23 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0027_remove_home_twitter_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="home",
            name="facebook_url",
            field=models.CharField(blank=True, default="", max_length=2083, null=True),
        ),
        migrations.AlterField(
            model_name="home",
            name="instagram_url",
            field=models.CharField(blank=True, default="", max_length=2083, null=True),
        ),
        migrations.AlterField(
            model_name="home",
            name="whatsapp_url",
            field=models.CharField(blank=True, default="", max_length=2083, null=True),
        ),
    ]
