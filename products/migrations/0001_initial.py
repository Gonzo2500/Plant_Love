# Generated by Django 3.2.4 on 2021-06-13 17:02

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_code', models.CharField(default=uuid.uuid4, editable=False, max_length=36)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('avg_rating', models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=2, null=True, verbose_name='average product rating')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('many_colors', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], help_text='Will the product come in multiple colors?', max_length=1)),
                ('main_pic', models.ImageField(blank=True, null=True, upload_to='', verbose_name='thumbnail picture')),
                ('pic2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='additional picture 2')),
                ('pic3', models.ImageField(blank=True, null=True, upload_to='', verbose_name='additional picture 3')),
                ('pic4', models.ImageField(blank=True, null=True, upload_to='', verbose_name='additional picture 4')),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('release_date', models.DateTimeField(help_text='Select today/now as the input if the product is being published now.', verbose_name='product release date')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('color_hex', colorfield.fields.ColorField(default='#FFFFFF', max_length=18)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]