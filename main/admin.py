from django.contrib import admin
from .models import Course, Teacher, Quantitative_indicator, Reason, Company, Contact, Reservations
from django.utils.safestring import mark_safe

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'desc', 'photo_img_tag', 'sort', 'is_visible')
    list_display_links = ('id', 'name')
    list_editable = ('price', 'desc', 'sort', 'is_visible')

    def photo_img_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width='50px'>")

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'photo_img_tag', 'sort', 'is_visible')
    list_display_links = ('id', 'name')
    list_editable = ('sort', 'is_visible')

    def photo_img_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width='50px'>")

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'job_title', 'desc', 'photo_img_tag', 'is_visible', 'sort')
    list_display_links = ('id',)
    list_editable = ('first_name', 'last_name', 'job_title', 'desc', 'is_visible', 'sort')

    def photo_img_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width='50px'>")

@admin.register(Quantitative_indicator)
class Quantitative_indicatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'indicator', 'value', 'is_visible', 'sort')
    list_display_links = ('id', 'indicator')
    list_editable = ('value', 'is_visible', 'sort')

@admin.register(Reason)
class ReasonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'desc', 'is_visible', 'sort')
    list_display_links = ('id',)
    list_editable = ('name', 'desc', 'is_visible', 'sort')

# class ContactAdmin(admin.ModelAdmin):
#     list_display = ('id', 'address', 'reservation', 'opening_hours'),
#     list_display_links = ('id')
#     list_editable = ('address', 'reservation', 'opening_hours').+



admin.site.register(Contact)
admin.site.register(Reservations)