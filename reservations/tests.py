from datetime import date, time

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Reservation


class ReservationCRUDTests(TestCase):
    def setUp(self):
        # Create two users
        self.user1 = User.objects.create_user(username="user1", password="pass123")
        self.user2 = User.objects.create_user(username="user2", password="pass123")

        # Log in user1 by default
        self.client.login(username="user1", password="pass123")

        # Create a reservation for user1
        self.reservation = Reservation.objects.create(
            name="Test Name",
            phone=1234567890,  # stored as int on the model
            email="test@example.com",
            date=date(2025, 8, 10),
            time=time(19, 30),
            number_of_people=4,
            user=self.user1,
        )

    def test_create_reservation(self):
        """Test creating a reservation via POST to the list view."""
        response = self.client.post(
            reverse("reservation:reservation_list"),
            {
                "name": "New Reservation",
                "phone": "0987654321",
                "email": "new@example.com",
                "date": "2025-08-11",
                "time": "20:00",
                "number_of_people": 2,
            },
        )
        # Successful create redirects back to the list
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Reservation.objects.count(), 2)

    def test_update_reservation(self):
        """Owner can update their reservation."""
        response = self.client.post(
            reverse("reservation:reservation_update", args=[self.reservation.id]),
            {
                "name": "Updated Name",
                "phone": "1234567890",
                "email": "updated@example.com",
                "date": "2025-08-10",
                "time": "19:30",
                "number_of_people": 5,
            },
        )
        # Successful update redirects back to the list
        self.assertEqual(response.status_code, 302)
        self.reservation.refresh_from_db()
        self.assertEqual(self.reservation.name, "Updated Name")

    def test_delete_reservation(self):
        """Owner can delete their reservation."""
        response = self.client.post(
            reverse("reservation:reservation_delete", args=[self.reservation.id])
        )
        # Successful delete redirects back to the list
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Reservation.objects.filter(id=self.reservation.id).exists())

    def test_user_cannot_edit_other_users_reservation(self):
        """Different user gets 404 when trying to edit someone else's reservation."""
        self.client.logout()
        self.client.login(username="user2", password="pass123")
        response = self.client.post(
            reverse("reservation:reservation_update", args=[self.reservation.id]),
            {
                "name": "Hacker Attempt",
                "phone": "0000000000",
                "email": "hack@example.com",
                "date": "2025-08-10",
                "time": "19:30",
                "number_of_people": 1,
            },
        )
        # Because the view uses get_object_or_404(pk=..., user=request.user)
        # user2 should see a 404 (not found).
        self.assertEqual(response.status_code, 404)
        self.reservation.refresh_from_db()
        self.assertNotEqual(self.reservation.name, "Hacker Attempt")
