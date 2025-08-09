from django.shortcuts import render, redirect
from .models import Reservation
from .forms import ReservationForm

def reservation_list(request):
    reservation_details = {}  # Initialize it here for safety

    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()  # Save to the database
            reservation_details = {
                'name': reservation.name,
                'date': reservation.date.strftime('%A, %B %d, %Y'),  # Example: "Saturday, February 17, 2025"
                'time': reservation.time.strftime('%I:%M %p'),  # Example: "07:30 PM"
                'people': reservation.number_of_people
            }
            form = ReservationForm()  # Reset form after successful booking
            # Redirect to the same page to avoid resubmitting the form when reloading
            return redirect('reservation:reservation_list')

    else:
        form = ReservationForm()

    # Fetch all reservations from the database
    reservations = Reservation.objects.all()

    return render(request, 'reservations/reservation_list.html', {'form': form, 'reservations': reservations, 'reservation_details': reservation_details})
