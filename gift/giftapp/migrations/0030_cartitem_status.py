# Generated by Django 4.2.5 on 2023-10-04 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giftapp', '0029_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='status',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
