# Generated by Django 2.0.7 on 2018-09-09 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samuv_site', '0004_auto_20180909_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagem',
            name='imageName',
            field=models.CharField(default='IMG09092018050436', max_length=80),
        ),
    ]
