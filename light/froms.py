from django import forms
from .models import Light


class LightFom(forms.ModelForm):

    class Meta:
        model = Light
        fields = "__all__"
