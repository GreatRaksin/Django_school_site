from django import forms
from .models import Tutor

class TutorSelectForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ('office', 'subject')

        widgets = {
            'office': forms.Select(attrs={'class': 'form-select'}),
            'subject': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, subject=None, city=None):
        super().__init__()
        if subject and city:
            self.fields['subject', 'office'].queryset = Tutor.objects.filter(office=city, subject=subject)