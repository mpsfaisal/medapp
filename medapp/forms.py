from django import forms
from . import models

class Reg_patient(forms.ModelForm):
    class Meta:
        model=models.patient_details
        fields=['name','phone','gender','address','consulting_date','history','observations','remedy','next_consultation','entry_by']
    