from django import forms
from .models import urlModel
from django.core.exceptions import ValidationError

class urlForm(forms.ModelForm):

    class Meta:
        model = urlModel
        fields = ['url','miniurl']
        widgets = {
            'url' : forms.TextInput(attrs={'class': "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",'placeholder' : 'Paste your original URL'}),
            'miniurl' : forms.TextInput(attrs={'class': "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",'placeholder' : 'Enter Your desired MiniURL'})
        }
        error_messages = {
            'miniurl': {'unique': "Oops!! This MiniURL is Already Taken :) ",'invalid': "MiniURL should only contain alphabetic characters!",},
        }

    def clean(self):
        cleaned_data = super().clean()
        url = cleaned_data.get('url')
        miniurl = cleaned_data.get('miniurl')

        if not miniurl.isalpha():
            raise ValidationError(("MiniURL should only contain alphabetic characters!"), code='invalid')
        if not miniurl:
            raise ValidationError("Your field is required.")
        if not url:
            raise ValidationError("This field is required.")

        return cleaned_data
    