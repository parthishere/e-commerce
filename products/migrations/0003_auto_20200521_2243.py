# Generated by Django 3.0.4 on 2020-05-21 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='default/images.png', upload_to='products/'),
        ),
    ]
