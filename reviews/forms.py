from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'title', 'body']  # Include all the necessary fields

        widgets = {
            'body': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your review...'}),
        }
