# Generated by Django 3.2.5 on 2021-07-21 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainweb', '0002_products_prodimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='prodimg',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
