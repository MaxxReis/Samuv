# Generated by Django 2.0.7 on 2018-11-22 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('samuv_site', '0042_auto_20181122_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='profissional',
            name='clinica',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='samuv_site.Clinica'),
        ),
        migrations.AlterField(
            model_name='imagem',
            name='imageName',
            field=models.CharField(default='IMG22112018033313', max_length=80),
        ),
    ]
