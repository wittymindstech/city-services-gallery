# Generated by Django 3.1.10 on 2021-08-24 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coreApp', '0006_auto_20210824_1103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicemodel',
            name='provided_by',
        ),
        migrations.AddField(
            model_name='servicemodel',
            name='provided_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='coreApp.businessprofilemodel'),
            preserve_default=False,
        ),
    ]
