from django import forms

from .models import Profile
INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border text-red-700'

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'age_limit')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'age_limit': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),

        }