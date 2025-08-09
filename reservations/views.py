from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Reservation
from .forms import ReservationForm


@login_required
def reservation_list(request):
    # Create
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user  # link to owner
            reservation.save()
            messages.success(request, "Your reservation was created successfully.")
            return redirect('reservation:reservation_list')
    else:
        form = ReservationForm()

    # Read (only the current user's reservations)
    reservations = (
        Reservation.objects.filter(user=request.user)
        .order_by('-date', '-time')
    )

    return render(
        request,
        'reservations/reservation_list.html',
        {
            'form': form,
            'reservations': reservations,
            'reservation_details': {},  # kept for template compatibility
        },
    )


@login_required
def reservation_update(request, pk):
    # Only allow the owner to update
    reservation = get_object_or_404(Reservation, pk=pk, user=request.user)

    if request.method == "POST":
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            messages.success(request, "Reservation updated.")
            return redirect('reservation:reservation_list')
    else:
        form = ReservationForm(instance=reservation)

    return render(
        request,
        'reservations/reservation_form.html',
        {'form': form, 'object': reservation},
    )


@login_required
def reservation_delete(request, pk):
    # Only allow the owner to delete
    reservation = get_object_or_404(Reservation, pk=pk, user=request.user)

    if request.method == "POST":
        reservation.delete()
        messages.success(request, "Reservation deleted.")
        return redirect('reservation:reservation_list')

    return render(
        request,
        'reservations/reservation_confirm_delete.html',
        {'object': reservation},
    )