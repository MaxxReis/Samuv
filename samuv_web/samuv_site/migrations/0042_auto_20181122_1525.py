# Generated by Django 2.0.7 on 2018-11-22 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samuv_site', '0041_auto_20181117_0941'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clinica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('endereco', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Clinica',
                'verbose_name_plural': 'Clinicas',
            },
        ),
        migrations.AlterField(
            model_name='imagem',
            name='imageName',
            field=models.CharField(default='IMG22112018032542', max_length=80),
        ),
    ]
