# Generated by Django 4.2.5 on 2023-10-04 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('giftapp', '0025_billinginformation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billinginformation',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='giftapp.userprofile'),
        ),
    ]
