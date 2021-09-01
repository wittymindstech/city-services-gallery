from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager
from django_resized import ResizedImageField
from django.conf import settings
from django.utils.text import slugify

WEEKDAYS = (
    ('1','Monday'),
    ('2','Tuesday'),
    ('3','Wednesday'),
    ('4','Thursday'),
    ('5','Friday'),
    ('6','Satday'),
    ('7','Sunday'),
)

class CategoyModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    thumbnail = ResizedImageField(size=[400, 400], quality=75,
                            crop=['middle', 'center'],
                            upload_to='categories/thumbnails',
                            null=True, blank=True)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class AmenitiesModel(models.Model):
    title = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Amenity'
        verbose_name_plural = 'Amenities'
    
    def __str__(self):
        return self.title


class BusinessProfileModel(models.Model):
    """
    Business model holds all the Businesses to be registered for app

    """

    account = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    business_name = models.CharField(max_length=100,help_text='How people can recognize you?')
    business_description = models.TextField(max_length=2000, blank=True, null=True, help_text='Tell us more about your business...')
    is_verified = models.BooleanField(default=False)
    category = models.ManyToManyField(CategoyModel)
    thumbnail = ResizedImageField(size=[400, 300], quality=75,
                                crop=['middle', 'center'],
                                upload_to='businesses/thumbnails',
                                null=True, blank=True)
    # thumbnail = models.ImageField(upload_to='thumbnails/images', null=True, blank=True) #TODO: require attention # default='img/profile.png')
    landmark = models.CharField(max_length=200, blank=True, null=True)
    area_local = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=50,default='India')
    state = models.CharField(max_length=50,)
    city = models.CharField(max_length=50,default='Siwan')
    pincode = models.PositiveBigIntegerField(blank=True, null=True)
    mobile = models.BigIntegerField(blank=True, null=True)
    registered_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=80, unique=True)
    amenities = models.ManyToManyField(AmenitiesModel,)
    status = models.CharField(choices=(('O', 'Open'), ('C', 'Closed'),), max_length=1, default='C')
    class Meta:
        verbose_name = 'Business'
        verbose_name_plural = 'Businesses'
    
    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.file.delete(save=False)
        self.thumbnail.delete(save=False)
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"{self.account} || {self.business_name}"
    
    @property
    def calculate_ratings(self):
        return 5
    
class OpeningHoursModel(models.Model):
    business = models.ForeignKey(BusinessProfileModel, on_delete=models.CASCADE)
    weekday = models.CharField(max_length=1, choices=WEEKDAYS,unique=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        verbose_name = 'Opening Hours'
        verbose_name_plural = 'Opening Hours'

    def __str__(self):
        return f"{self.business} || {self.get_weekday_display()}"
class ServiceModel(models.Model):
    provided_by = models.ForeignKey(BusinessProfileModel,on_delete=models.CASCADE)
    service_name = models.CharField(max_length=200, verbose_name='title')
    service_description = models.CharField(max_length=2000, verbose_name='description')
    tag = TaggableManager()
    liked_by = models.ManyToManyField(User,) #TODO: Later to be changed into default
    thumbnail = ResizedImageField(size=[400, 400], quality=75,
                                crop=['middle', 'center'],
                                upload_to='musics/thumbnails',)
                                # default='img/9.jpg') #TODO: default thumbnail to be select
    slug = models.SlugField(max_length=80, unique=True)
    
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
    
    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.file.delete(save=False)
        self.thumbnail.delete(save=False)
        super().delete(*args, **kwargs)

    def __str__(self):
        return f'{self.provided_by} || {self.service_name}'

class ReviewModel(models.Model):
    account = models.ForeignKey(User, on_delete=models.SET_NULL , null=True) #TODO: Later to be changed into default
    business = models.ManyToManyField(BusinessProfileModel, )
    service = models.ManyToManyField(ServiceModel,)
    image = ResizedImageField(size=[400, 400], 
                        quality=75, crop=['middle', 'center'],
                        upload_to='musics/thumbnails',
                        null=True, blank=True)
    review_text = models.CharField(max_length=2000,)
    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
    def __str__(self):
        return f"{self.account} || {self.business}"
