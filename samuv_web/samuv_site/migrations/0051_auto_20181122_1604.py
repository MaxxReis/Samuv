# Generated by Django 2.0.7 on 2018-11-22 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samuv_site', '0050_auto_20181122_1604'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Clinica',
        ),
        migrations.AlterField(
            model_name='imagem',
            name='imageName',
            field=models.CharField(default='IMG22112018040430', max_length=80),
        ),
    ]
