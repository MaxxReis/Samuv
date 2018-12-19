# Generated by Django 2.0.7 on 2018-11-17 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('samuv_site', '0040_auto_20181116_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='atendimento',
            name='tecnica',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='samuv_site.Tecnica'),
        ),
        migrations.AlterField(
            model_name='imagem',
            name='imageName',
            field=models.CharField(default='IMG17112018094135', max_length=80),
        ),
    ]
