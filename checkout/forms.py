from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    Order form to be used in checkout to display
    and capture user information
    """
    class Meta:
        model = Order
        # exclude = ['delivery_type']
        fields = ['first_name', 'last_name', 'email',
                  'phone_number', 'address_line_1',
                  'address_line_2', 'city', 'region',
                  'country', 'postcode', 'delivery_type']

    def __init__(self, *args, **kwargs):
        """
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'E-mail',
            'phone_number': 'Phone Number',
            'address_line_1': 'Address Line 1',
            'address_line_2': 'Address Line 2',
            'city': 'City/Town',
            'region': 'Region/County/State',
            'postcode': 'Post/ZIP Code',
            'delivery_type': 'Delivery Type'
        }

        self.fields['email'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country' and field != 'delivery_type':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style'
            self.fields[field].label = False