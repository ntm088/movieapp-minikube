from django import forms
from .models import Video
from datetime import datetime

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = [
    'MovieTitle','Actor1Name','Actor2Name',
    'DirectorName','MovieGenre','ReleaseYear',
    'DurationMinutes'  
]
        widgets = {
            'MovieTitle': forms.TextInput(attrs={'class': 'input'}),
            'Actor1Name': forms.TextInput(attrs={'class': 'input'}),
            'Actor2Name': forms.TextInput(attrs={'class': 'input'}),
            'DirectorName': forms.TextInput(attrs={'class': 'input'}),
            'MovieGenre': forms.Select(attrs={'class': 'input'}),
            'ReleaseYear': forms.NumberInput(attrs={'class': 'input', 'min': 1880, 'max': datetime.now().year}),
            'DurationMinutes': forms.NumberInput(attrs={'class': 'input', 'min': 1, 'max': 500}),
        }

    def clean_ReleaseYear(self):
        y = self.cleaned_data['ReleaseYear']
        if y < 1880 or y > datetime.now().year:
            raise forms.ValidationError("Enter a valid release year.")
        return y
