# Generated by Django 4.2.5 on 2023-09-26 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giftapp', '0023_remove_communityprofile_is_approval_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='communityprofile',
            name='is_approval',
            field=models.BooleanField(default=False),
        ),
    ]
