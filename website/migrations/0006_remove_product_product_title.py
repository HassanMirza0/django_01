# Generated by Django 4.2.4 on 2023-09-01 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_rename_category_product_brand_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_title',
        ),
    ]
