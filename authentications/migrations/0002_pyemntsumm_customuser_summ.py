# Generated by Django 4.2.7 on 2023-11-09 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentications', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PyemntSumm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summ', models.FloatField()),
                ('days', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='summ',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
