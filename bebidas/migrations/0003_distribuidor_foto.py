# Generated by Django 3.1.5 on 2021-05-22 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bebidas', '0002_auto_20210522_0944'),
    ]

    operations = [
        migrations.AddField(
            model_name='distribuidor',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes'),
        ),
    ]