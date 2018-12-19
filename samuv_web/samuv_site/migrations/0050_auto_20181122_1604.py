# Generated by Django 2.0.7 on 2018-11-22 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('samuv_site', '0049_auto_20181122_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profissional',
            name='clinica',
        ),
        migrations.AlterField(
            model_name='imagem',
            name='imageName',
            field=models.CharField(default='IMG22112018040359', max_length=80),
        ),
        migrations.AlterField(
            model_name='profissional',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samuv_site.Usuario'),
        ),
    ]
