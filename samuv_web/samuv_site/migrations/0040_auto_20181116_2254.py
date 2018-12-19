# Generated by Django 2.0.7 on 2018-11-17 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('samuv_site', '0039_auto_20181116_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='atendimento',
            name='profissional',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='samuv_site.Profissional'),
        ),
        migrations.AlterField(
            model_name='imagem',
            name='imageName',
            field=models.CharField(default='IMG16112018105455', max_length=80),
        ),
    ]
