# Generated by Django 4.2.5 on 2023-09-30 10:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('giftapp', '0024_communityprofile_is_approval'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('town', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=10)),
                ('payment_status', models.BooleanField(default=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('product', models.ManyToManyField(blank=True, to='giftapp.product')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
