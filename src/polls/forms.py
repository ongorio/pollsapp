from django import forms

from polls.models import Poll, Option

class PollForm(forms.Form):
    title = forms.CharField(label='Title', max_length=255, min_length=2, required=True)
    description = forms.CharField(label='Description' ,max_length=255, widget=forms.Textarea())
    options = forms.CharField(label='Options', max_length=8000, required=True, help_text='Separate options using new Line', widget=forms.Textarea(attrs={'rows': 8}))

