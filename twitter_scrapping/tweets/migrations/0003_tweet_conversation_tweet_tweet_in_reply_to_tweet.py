# Generated by Django 4.1.7 on 2023-03-16 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("tweets", "0002_rename_in_reply_to_tweet_conversation_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="tweet",
            name="conversation_tweet",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="conversation_tweets_set",
                to="tweets.tweet",
            ),
        ),
        migrations.AddField(
            model_name="tweet",
            name="in_reply_to_tweet",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="tweet_replies_set",
                to="tweets.tweet",
            ),
        ),
    ]
