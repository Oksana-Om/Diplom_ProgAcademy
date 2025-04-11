from django.db import models
from ckeditor.fields import RichTextField


class Course(models.Model):

    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    desc = models.TextField(max_length=255, unique=True)
    photo = models.ImageField(upload_to='courses/')

    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    class Meta:
        db_table = 'main_courses'
        ordering = ('sort', 'name')
        verbose_name = 'Курс'
        verbose_name_plural = 'courses'

    def __str__(self):
        return self.name

class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    job_title = models.CharField(max_length=40)
    desc = models.TextField(max_length=500)
    photo = models.ImageField(upload_to='staff/')

    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    def __str__(self):
        return self.last_name

class Quantitative_indicator(models.Model):
    indicator = models.CharField(max_length=50)
    value = models.IntegerField(default=0)
    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    def __str__(self):
        return self.indicator
    class Meta:
        db_table = 'quantitative_indicators'

class Reason(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField(max_length=500)
    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'reasons'

# class Feature(models.Model):
#     name = models.CharField(max_length=150)
#     sign_name = models.CharField(max_length=50)
#     is_visible = models.BooleanField(default=True)
#     sort = models.IntegerField(default=0)
#     class Meta:
#         db_table = 'features'

class Company(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='companies/')
    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'companies'

class Contact(models.Model):
    address = RichTextField()
    reservation = RichTextField()
    opening_hours = RichTextField()

class Reservations(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=500)

    is_confirmed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'main_reservations'
        ordering = ('-date_created',)

