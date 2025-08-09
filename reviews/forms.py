from django import forms
from django.core.exceptions import ValidationError

from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["title", "rating", "body"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "rating": forms.Select(attrs={"class": "form-control"}),
            "body": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        }

    def clean_rating(self):
        r = int(self.cleaned_data["rating"])
        if not (1 <= r <= 5):
            raise ValidationError("Rating must be between 1 and 5.")
        return r
