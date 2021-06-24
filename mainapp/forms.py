from django import forms

from mainapp.models import Plant


class AddPlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ('category', 'title', 'description', 'place_of_purchase', 'price',)

