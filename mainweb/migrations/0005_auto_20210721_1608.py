# Generated by Django 3.2.5 on 2021-07-21 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainweb', '0004_alter_products_prodimg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='prodimg',
        ),
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(default=0, upload_to='product/'),
            preserve_default=False,
        ),
    ]
