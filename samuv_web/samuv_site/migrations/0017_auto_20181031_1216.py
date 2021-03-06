# Generated by Django 2.0.7 on 2018-10-31 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samuv_site', '0016_auto_20181031_1150'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anamnese',
            options={'verbose_name': 'Anamnese', 'verbose_name_plural': 'Anamneses'},
        ),
        migrations.AlterField(
            model_name='imagem',
            name='imageName',
            field=models.CharField(default='IMG31102018121614', max_length=80),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='condicaoSaneamento',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='escolaridade',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='estadoCivil',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='habilitacao',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='profissao',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='religiao',
            field=models.CharField(default='', max_length=250),
        ),
    ]
