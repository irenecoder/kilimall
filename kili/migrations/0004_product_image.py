# Generated by Django 4.1.4 on 2022-12-31 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kili', '0003_alter_product_options_product_available_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d'),
        ),
    ]
