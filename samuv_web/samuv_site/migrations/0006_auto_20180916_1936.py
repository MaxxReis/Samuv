# Generated by Django 2.0.7 on 2018-09-16 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samuv_site', '0005_auto_20180909_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagem',
            name='marked_image',
            field=models.ImageField(blank=True, null=True, upload_to='imagens_marcadas/'),
        ),
        migrations.AlterField(
            model_name='imagem',
            name='imageName',
            field=models.CharField(default='IMG16092018073607', max_length=80),
        ),
    ]
