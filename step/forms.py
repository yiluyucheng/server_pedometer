from django import forms


Sex_CHOICES = (('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others'))


class StepForm(forms.Form):
    ids = forms.CharField(label='Unique ID', max_length=100)
    Date = forms.CharField(label='Date', max_length=20)
    Start = forms.CharField(label='Start time', max_length=30)
    End = forms.CharField(label='End time', max_length=30)
    Step = forms.IntegerField(label='Step count', required=False)
    Distance = forms.FloatField(label='Distance', required=False)
    Pain = forms.IntegerField(label='Feeling of Pain', required=False)
    
    Height = forms.IntegerField(label='Height')
    Weight = forms.FloatField(label='Weight')
    Sex = forms.CharField(max_length=10, label='Sex')
    Sex = forms.CharField(label="Sex", widget=forms.RadioSelect(choices=Sex_CHOICES))
    Age = forms.FloatField(label='Age')