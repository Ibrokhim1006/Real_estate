# Generated by Django 4.2.7 on 2023-11-09 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate', '0002_adsubcategory_id_ad_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realestetimgaes',
            name='real_estet_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='img', to='real_estate.realestate'),
        ),
    ]
