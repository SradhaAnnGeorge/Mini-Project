# Generated by Django 4.2.4 on 2023-09-06 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giftapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('description', models.CharField(default='', max_length=200)),
                ('image', models.ImageField(upload_to='products/')),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
