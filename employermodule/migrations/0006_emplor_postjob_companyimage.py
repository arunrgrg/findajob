# Generated by Django 3.2.8 on 2021-12-26 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employermodule', '0005_rename_simg_em_img_eimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='emplor_postjob',
            name='companyimage',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
