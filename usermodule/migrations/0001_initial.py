# Generated by Django 3.2.8 on 2021-12-21 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='seeker_img',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('simg', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='seeker_resum',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('stitle', models.CharField(max_length=100)),
                ('sskill1', models.CharField(max_length=50)),
                ('sskill2', models.CharField(max_length=50)),
                ('sskill3', models.CharField(max_length=50)),
                ('sskill4', models.CharField(max_length=50)),
                ('sabout', models.CharField(max_length=150)),
                ('sschoolname', models.CharField(max_length=50)),
                ('squalification', models.CharField(max_length=50)),
                ('scompany', models.CharField(max_length=50)),
                ('srole', models.CharField(max_length=50)),
                ('sstartdate', models.CharField(max_length=20)),
                ('senddate', models.CharField(max_length=20)),
            ],
        ),
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
