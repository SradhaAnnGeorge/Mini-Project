# Generated by Django 4.2.5 on 2023-09-14 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giftapp', '0007_userprofile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=225, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
