from django import forms

    
class StepForm(forms.Form):
    ids = forms.CharField(label='Unique ID', max_length=100)
    Step = forms.IntegerField(label='Count', required=False)
    Pain = forms.IntegerField(label='Pain', required=False)
