# Generated by Django 2.0.6 on 2018-06-16 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('montesory', '0003_auto_20180616_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pic',
            field=models.FileField(upload_to=''),
        ),
    ]