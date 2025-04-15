from .models import Contact

def app_title(request):
    return {
        'title': 'IT school<span></span>'
    }

def footer (request):
    res = Contact.objects.first()
    return {
        'address': res.address,
        'for_reservation': res.for_reservation,
        'opening_hours': res.opening_hours,


    }