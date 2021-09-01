# Generated by Django 3.1.10 on 2021-09-01 05:46

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('coreApp', '0008_auto_20210901_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoymodel',
            name='thumbnail',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=75, size=[400, 400], upload_to='categories/thumbnails'),
        ),
    ]