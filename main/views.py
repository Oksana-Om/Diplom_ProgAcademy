from django.shortcuts import render
from .models import  Course, Teacher, Quantitative_indicator, Reason, Company
# Category,

def index(request):
    # categories = Category.objects.filter(is_visible=True)
    teachers = Teacher.objects.filter(is_visible=True)
    quantitative_indicators = Quantitative_indicator.objects.filter(is_visible=True)
    reasons = Reason.objects.filter(is_visible=True)
    courses = Course.objects.filter(is_visible=True)
    companies = Company.objects.filter(is_visible=True)
    context = {
        # 'categories': categories,
        'teachers': teachers,
        'quantitative_indicators': quantitative_indicators,
        'reasons': reasons,
        'courses': courses,
        'companies': companies,

    }

    return render(request, 'index.html', context=context)

    #return render(request, 'index.html')
