# Generated by Django 4.1.7 on 2023-03-24 21:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tweets", "0005_tweet_scrapping_request"),
    ]

    operations = [
        migrations.AddField(
            model_name="scrappingrequest",
            name="recurse",
            field=models.BooleanField(default=False),
        ),
    ]
