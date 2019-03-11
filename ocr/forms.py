from django import forms


class UrlForm(forms.Form):
    url = forms.URLField(widget=forms.URLInput(attrs={'class': 'fullWidth'}))
