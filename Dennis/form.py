from django import forms
from Dennis.model import Students


class EmpForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = "__all__"
