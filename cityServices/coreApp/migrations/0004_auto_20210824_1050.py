# Generated by Django 3.1.10 on 2021-08-24 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreApp', '0003_auto_20210822_0017'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AlterModelOptions(
            name='amenitiesmodel',
            options={'verbose_name': 'Amenity', 'verbose_name_plural': 'Amenities'},
        ),
        migrations.AlterModelOptions(
            name='businessprofilemodel',
            options={'verbose_name': 'Business', 'verbose_name_plural': 'Businesses'},
        ),
        migrations.AlterModelOptions(
            name='openinghoursmodel',
            options={'verbose_name': 'Opening Hours', 'verbose_name_plural': 'Opening Hours'},
        ),
        migrations.AlterModelOptions(
            name='reviewmodel',
            options={'verbose_name': 'Review', 'verbose_name_plural': 'Reviews'},
        ),
        migrations.AlterModelOptions(
            name='servicemodel',
            options={'verbose_name': 'Service', 'verbose_name_plural': 'Services'},
        ),
    ]
