# Generated by Django 4.2.5 on 2023-10-04 09:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('giftapp', '0027_alter_billinginformation_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billinginformation',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
