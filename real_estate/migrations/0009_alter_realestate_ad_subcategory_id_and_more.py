# Generated by Django 4.2.7 on 2023-11-10 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate', '0008_alter_realestate_amenities_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realestate',
            name='ad_subcategory_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='real_estate.adsubcategory'),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='ad_taype_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='real_estate.adtype'),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='build_mateial_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='real_estate.buildmaterial'),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='category_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='real_estate.categoriesrealestet'),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='currency_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='real_estate.currency'),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='distric_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='real_estate.distric'),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='repair_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='real_estate.repair'),
        ),
    ]
