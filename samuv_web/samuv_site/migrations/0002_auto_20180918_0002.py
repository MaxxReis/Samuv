# Generated by Django 2.0.7 on 2018-09-18 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samuv_site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='cpf',
            field=models.CharField(blank=True, max_length=14, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='foto',
            field=models.ImageField(default=1, upload_to='imagens/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='imagem',
            name='imageName',
            field=models.CharField(default='IMG18092018120028', max_length=80),
        ),
    ]
