# Generated by Django 3.2.8 on 2022-01-17 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employermodule', '0015_alter_mail_msg_employer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emplor_postjob',
            name='jobcategory',
            field=models.CharField(choices=[('Real Estate', 'Real Estate'), ('marketing', 'marketing'), ('education', 'education'), ('healthcare', 'healthcare'), ('science', 'science'), ('Technologies', 'Technologies'), ('Design', 'Design'), ('food services', 'food services')], max_length=50, null=True),
        ),
    ]
