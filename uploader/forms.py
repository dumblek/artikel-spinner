from django import forms

# Create your forms here.

class ExampleForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea)