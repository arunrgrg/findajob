# Generated by Django 3.2.8 on 2022-01-04 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermodule', '0006_auto_20211230_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog_se',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('imgblog', models.CharField(max_length=200, null=True)),
                ('jobtext', models.CharField(max_length=1500, null=True)),
                ('employerblog', models.CharField(max_length=150, null=True)),
                ('seekerblog', models.CharField(max_length=150, null=True)),
            ],
        ),
    ]