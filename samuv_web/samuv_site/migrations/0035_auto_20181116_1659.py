# Generated by Django 2.0.7 on 2018-11-16 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samuv_site', '0034_auto_20181116_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitospessoais',
            name='alergiaTopica',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='habitospessoais',
            name='etilismo',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='habitospessoais',
            name='tabagismo',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='imagem',
            name='imageName',
            field=models.CharField(default='IMG16112018045916', max_length=80),
        ),
    ]
