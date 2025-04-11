from django.shortcuts import render, redirect
from .models import Course, Teacher, Quantitative_indicator, Reason, Company, Contact, Reservations
from .forms import ReservationForm
from django.http import HttpResponse
from django.contrib import messages




def index(request):
    # categories = Category.objects.filter(is_visible=True)
    teachers = Teacher.objects.filter(is_visible=True)
    quantitative_indicators = Quantitative_indicator.objects.filter(is_visible=True)
    reasons = Reason.objects.filter(is_visible=True)
    courses = Course.objects.filter(is_visible=True)
    companies = Company.objects.filter(is_visible=True)
    # contacts = Contact.objects.filter(is_visible=True)
    reservation = ReservationForm(request.POST or None)

    if request.method == 'POST' and reservation.is_valid():
        reservation.save()
        messages.success(request, 'Your reservation has been saved. Wait for a call')
        return redirect('home')



    context = {
        # 'categories': categories,
        'teachers': teachers,
        'quantitative_indicators': quantitative_indicators,
        'reasons': reasons,
        'courses': courses,
        'companies': companies,
        'reservation': reservation,
        # 'contacts': contacts,

    }

    return render(request, 'index.html', context=context)

    #return render(request, 'index.html')
