# Generated by Django 3.2.8 on 2021-12-28 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employermodule', '0009_alter_emplor_postjob_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emplor_postjob',
            name='experiance',
            field=models.CharField(choices=[('1 year', '1 year'), ('1 to 5 yea', '1 to 5 yea'), ('5 to 10 year', '5 to 10 year'), ('10 to 20 year', '10 to 20 year')], max_length=50),
        ),
    ]