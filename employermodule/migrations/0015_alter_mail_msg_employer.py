# Generated by Django 3.2.8 on 2022-01-03 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employermodule', '0014_rename_mail_mail_msg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail_msg',
            name='employer',
            field=models.IntegerField(null=True),
        ),
    ]