# Generated by Django 3.0.7 on 2020-06-05 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=100),
        ),
    ]