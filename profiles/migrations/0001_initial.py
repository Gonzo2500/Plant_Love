# Generated by Django 3.2.4 on 2021-06-16 18:54

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('memberships', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_phone_number', models.CharField(blank=True, max_length=16, null=True, validators=[django.core.validators.RegexValidator(message="Enter phone number in a format:'+111111111' and no longer that 15 digits.", regex='^\\+?1?\\d{9,15}$')])),
                ('user_address_line_1', models.CharField(blank=True, max_length=100, null=True)),
                ('user_address_line_2', models.CharField(blank=True, max_length=100, null=True)),
                ('user_city', models.CharField(blank=True, max_length=85, null=True, verbose_name='city or town')),
                ('user_region', models.CharField(blank=True, max_length=85, null=True, verbose_name='region or county')),
                ('user_country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('user_postcode', models.CharField(blank=True, max_length=10, null=True, verbose_name='post/zip code')),
                ('membership', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='memberships.membership')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
