# Generated by Django 4.2.7 on 2023-11-09 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentications', '0002_pyemntsumm_customuser_summ'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pyemntsumm',
            name='days',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
