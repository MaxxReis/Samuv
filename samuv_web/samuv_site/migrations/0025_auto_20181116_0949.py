# Generated by Django 2.0.7 on 2018-11-16 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samuv_site', '0024_auto_20181116_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagem',
            name='imageName',
            field=models.CharField(default='IMG16112018094902', max_length=80),
        ),
    ]
