# reservations/forms.py
from django import forms
from django.core.exceptions import ValidationError
from datetime import date, time as dtime
from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["name", "phone", "email", "date", "time", "number_of_people"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            # Keep TextInput for better UX; we'll validate in clean_phone()
            "phone": forms.TextInput(attrs={"class": "form-control", "inputmode": "numeric"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            # HTML5 inputs help, but server-side validation is the source of truth
            "date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "time": forms.TimeInput(
                attrs={
                    "type": "time",
                    "class": "form-control",
                    "min": "08:00",
                    "max": "22:30",   # last slot
                    "step": "1800",   # 30 min in seconds
    }
),
            "number_of_people": forms.NumberInput(attrs={"class": "form-control", "min": 1}),
        }

    # --- Validations ---

    def clean_date(self):
        d = self.cleaned_data["date"]
        if d < date.today():
            raise ValidationError("Please choose a date today or in the future.")
        return d

    def clean_time(self):
        """
        Only allow 30-minute slots between 08:00 and 23:00 (inclusive bound),
        but with last valid *start* time at 22:30. So 23:00 is NOT valid.
        """
        t = self.cleaned_data["time"]

        # Must be on 00 or 30 minutes exactly
        if t.minute not in (0, 30) or t.second != 0 or t.microsecond != 0:
            raise ValidationError("Please choose a time in 30‑minute steps (e.g., 08:00, 08:30, 09:00).")

        # Earliest 08:00
        if t < dtime(hour=8, minute=0):
            raise ValidationError("We accept reservations from 08:00 onwards.")

        # Latest start 22:30 (so 23:00 is invalid)
        if t > dtime(hour=22, minute=30):
            raise ValidationError("The last available time is 22:30.")

        return t

    def clean_phone(self):
        """Allow digits only; normalize to int for the IntegerField on the model."""
        raw = str(self.cleaned_data.get("phone", "")).strip()
        digits = "".join(ch for ch in raw if ch.isdigit())

        if not digits:
            raise ValidationError("Phone number is required.")
        if not (7 <= len(digits) <= 15):
            raise ValidationError("Phone must be 7–15 digits.")

        try:
            return int(digits)
        except ValueError:
            raise ValidationError("Invalid phone number.")

    def clean_number_of_people(self):
        n = self.cleaned_data["number_of_people"]
        if n < 1:
            raise ValidationError("Please enter at least 1 guest.")
        return n