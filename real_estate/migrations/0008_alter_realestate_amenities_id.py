# Generated by Django 4.2.7 on 2023-11-09 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate', '0007_alter_realestate_author_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realestate',
            name='amenities_id',
            field=models.ManyToManyField(blank=True, null=True, to='real_estate.amenities'),
        ),
    ]