# Generated by Django 4.2.5 on 2023-10-09 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giftapp', '0030_cartitem_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100, null=True)),
                ('mobile', models.CharField(max_length=15)),
            ],
        ),
    ]
