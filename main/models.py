from django.db import models

# class Category(models.Model):
#
#     name = models.CharField(max_length=50, unique=True)
#     slug = models.SlugField(blank=True)
#     is_visible = models.BooleanField(default=True)
#     sort = models.IntegerField(default=0)
#
#     class Meta:
#         db_table = 'main_categories'
#         ordering = ('sort', 'name')
#         verbose_name = 'Категорія курсів'
#         verbose_name_plural = 'categories'
#
#     def __str__(self):
#         return self.name
#
#     def __iter__(self):
#         for course in self.courses.all():
#             yield course

class Course(models.Model):

    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    desc = models.TextField(max_length=255, unique=True)
   # photo = models.ImageField(upload_to='dishes/')
    photo = models.ImageField(upload_to='courses/')
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses')

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

