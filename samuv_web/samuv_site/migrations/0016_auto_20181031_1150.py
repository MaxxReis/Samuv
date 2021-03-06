# Generated by Django 2.0.7 on 2018-10-31 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samuv_site', '0015_auto_20181029_1509'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anamnese',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso', models.FloatField()),
                ('altura', models.FloatField()),
                ('antecedentesPessoais', models.CharField(max_length=250)),
                ('medicamentosEmUso', models.CharField(max_length=250)),
                ('historiaUlcera', models.CharField(max_length=250)),
                ('inicioPrimeiraUlcera', models.CharField(max_length=250)),
                ('fechamentoUlcera', models.IntegerField()),
                ('ulceraAtual', models.IntegerField()),
                ('presencaDeDor', models.CharField(max_length=250)),
                ('alivioDaDor', models.CharField(max_length=250)),
                ('tempoTratamento', models.CharField(max_length=250)),
                ('localTratamento', models.CharField(max_length=250)),
                ('frequenciaTrocaCurativos', models.CharField(max_length=250)),
                ('trocaCurativosFinalDeSemana', models.CharField(max_length=250)),
                ('interrupcaoTratamento', models.BooleanField()),
                ('motivoInterrupcao', models.CharField(max_length=250)),
                ('terapiaCompressiva', models.CharField(max_length=250)),
                ('cirurgiaVarize', models.CharField(max_length=250)),
                ('profissionalAcompanhante', models.CharField(max_length=250)),
                ('acessoCef', models.CharField(max_length=250)),
                ('internacao', models.BooleanField()),
                ('culturaSecrecao', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='paciente',
            name='condicaoSaneamento',
            field=models.CharField(default=0, max_length=250),
        ),
        migrations.AddField(
            model_name='paciente',
            name='escolaridade',
            field=models.CharField(default=0, max_length=250),
        ),
        migrations.AddField(
            model_name='paciente',
            name='estadoCivil',
            field=models.CharField(default=0, max_length=250),
        ),
        migrations.AddField(
            model_name='paciente',
            name='habilitacao',
            field=models.CharField(default=0, max_length=250),
        ),
        migrations.AddField(
            model_name='paciente',
            name='numeroFilhos',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='paciente',
            name='profissao',
            field=models.CharField(default=0, max_length=250),
        ),
        migrations.AddField(
            model_name='paciente',
            name='religiao',
            field=models.CharField(default=0, max_length=250),
        ),
        migrations.AddField(
            model_name='paciente',
            name='rendaFamiliar',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='imagem',
            name='imageName',
            field=models.CharField(default='IMG31102018115028', max_length=80),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='idade',
            field=models.IntegerField(),
        ),
    ]
