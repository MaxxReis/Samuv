# Generated by Django 2.0.7 on 2018-11-07 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samuv_site', '0022_auto_20181031_1518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='anamnese',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='clinico',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='habitoPessoal',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='observacao',
        ),
        migrations.AlterField(
            model_name='imagem',
            name='imageName',
            field=models.CharField(default='IMG07112018033949', max_length=80),
        ),
    ]
