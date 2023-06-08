from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    
    class Meta:
        model = Tarea
        fields = ("name","date_to_complete","description","priority",)
        widgets = {
            'date_to_complete': forms.DateInput(attrs={
                'type': 'date',
                'class': 'datepicker'
            })}