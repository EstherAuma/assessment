from django import forms
from .models import Customer

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name','date_of_birth','gender',
                  'country','district','town','zip_code','phone_number_1','phone_number_2','email' ] 