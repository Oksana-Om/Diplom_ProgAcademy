from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from main.models import Reservations

def reservations_list(request):
    reservations = Reservations.objects.all()
    return render(request, 'manager_page.html', {'reservations': reservations})

@require_POST
def confirm_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservations, id=reservation_id)
    reservation.is_confirmed = True
    reservation.save()
    return redirect('manager')
