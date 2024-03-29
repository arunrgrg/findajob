# Generated by Django 3.2.8 on 2021-12-24 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usermodule', '0002_delete_seeker_reg'),
    ]

    operations = [
        migrations.CreateModel(
            name='seeker_reg',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('sfirstname', models.CharField(max_length=50)),
                ('slastname', models.CharField(max_length=50, null=True)),
                ('semail', models.CharField(max_length=50)),
                ('spassword', models.CharField(max_length=100)),
                ('smobilenumber', models.CharField(max_length=100)),
                ('imgid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usermodule.seeker_img')),
                ('seekerid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usermodule.seeker_resum')),
            ],
        ),
    ]
