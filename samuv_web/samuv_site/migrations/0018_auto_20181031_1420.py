# Generated by Django 2.0.7 on 2018-10-31 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('samuv_site', '0017_auto_20181031_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='anamnese',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='samuv_site.Anamnese'),
        ),
        migrations.AlterField(
            model_name='anamnese',
            name='acessoCef',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='anamnese',
            name='alivioDaDor',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='anamnese',
            name='altura',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='anamnese',
            name='antecedentesPessoais',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='anamnese',
            name='cirurgiaVarize',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='anamnese',
            name='culturaSecrecao',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='anamnese',
            name='fechamentoUlcera',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='anamnese',
            name='frequenciaTrocaCurativos',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='anamnese',
            name='historiaUlcera',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='anamnese',
            name='inicioPrimeiraUlcera',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='anamnese',
            name='internacao',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='anamnese',
            name='localTratamento',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='anamnese',
            name='medicamentosEmUso',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='anamnese',
            name='motivoInterrupcao',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='anamnese',
            name='peso',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='anamnese',
            name='presencaDeDor',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='anamnese',
            name='profissionalAcompanhante',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='anamnese',
            name='tempoTratamento',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='anamnese',
            name='terapiaCompressiva',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='anamnese',
            name='trocaCurativosFinalDeSemana',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='anamnese',
            name='ulceraAtual',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='imagem',
            name='imageName',
            field=models.CharField(default='IMG31102018022041', max_length=80),
        ),
    ]
