# Generated by Django 2.0.6 on 2018-06-16 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('montesory', '0004_auto_20180616_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pic',
            field=models.ImageField(upload_to=''),
        ),
    ]
