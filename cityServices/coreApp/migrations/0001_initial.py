# Generated by Django 3.1.10 on 2021-08-21 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessProfileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(help_text='How people can recognize you?', max_length=100)),
                ('business_description', models.TextField(blank=True, help_text='Tell us more about your business...', max_length=2000, null=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='thumbnails/images')),
                ('landmark', models.CharField(blank=True, max_length=200, null=True)),
                ('area_local', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(default='India', max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(default='Siwan', max_length=50)),
                ('pincode', models.PositiveBigIntegerField(blank=True, null=True)),
                ('mobile', models.BigIntegerField(blank=True, null=True)),
                ('registered_on', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=80, unique=True)),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=200, verbose_name='title')),
                ('service_description', models.CharField(max_length=2000, verbose_name='description')),
                ('thumbnail', django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format=None, keep_meta=True, quality=75, size=[400, 400], upload_to='musics/thumbnails')),
                ('slug', models.SlugField(max_length=80, unique=True)),
                ('liked_by', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('provided_by', models.ManyToManyField(to='coreApp.BusinessProfileModel')),
                ('tag', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='ReviewModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.CharField(max_length=2000)),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('business', models.ManyToManyField(to='coreApp.BusinessProfileModel')),
                ('service', models.ManyToManyField(to='coreApp.ServiceModel')),
            ],
        ),
    ]
