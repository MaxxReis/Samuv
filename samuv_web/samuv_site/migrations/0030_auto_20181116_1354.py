# Generated by Django 2.0.7 on 2018-11-16 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samuv_site', '0029_auto_20181116_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagem',
            name='imageName',
            field=models.CharField(default='IMG16112018015436', max_length=80),
        ),
    ]
