from django import forms
from django.core.exceptions import ValidationError
from datetime import date
from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["name", "phone", "email", "date", "time", "number_of_people"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            # keep TextInput for nicer UX; we'll validate & convert in clean_phone()
            "phone": forms.TextInput(attrs={"class": "form-control", "inputmode": "numeric"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            # HTML5 date/time inputs prevent ambiguous formats
            "date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "time": forms.TimeInput(attrs={"type": "time", "class": "form-control"}),
            "number_of_people": forms.NumberInput(attrs={"class": "form-control", "min": 1}),
        }

    # --- Validations ---

    def clean_date(self):
        d = self.cleaned_data["date"]
        if d < date.today():
            raise ValidationError("Please choose a date today or in the future.")
        return d

    def clean_phone(self):
        """Allow only digits; convert to int for the IntegerField on the model."""
        raw = str(self.cleaned_data.get("phone", "")).strip()
        digits = "".join(ch for ch in raw if ch.isdigit())

        if not digits:
            raise ValidationError("Phone number is required.")
        if not digits.isdigit():
            raise ValidationError("Phone must contain digits only.")
        if not (7 <= len(digits) <= 15):
            raise ValidationError("Phone must be 7–15 digits.")

        # Return int because the model field is IntegerField
        try:
            return int(digits)
        except ValueError:
            raise ValidationError("Invalid phone number.")

    def clean_number_of_people(self):
        n = self.cleaned_data["number_of_people"]
        if n < 1:
            raise ValidationError("Please enter at least 1 guest.")
        # Optional: cap at 12 or whatever your venue supports
        # if n > 12:
        #     raise ValidationError("For parties over 12, please call the restaurant.")
        return n