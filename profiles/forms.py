from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    """
    Create a form containing User Profile details
    """
    class Meta:
        model = Profile
        exclude = ('user', 'membership',)

    def __init__(self, *args, **kwargs):
        """
        Create placeholders for all the profile fields
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'user_phone_number': 'Phone Number',
            'user_address_line_1': 'Address Line 1',
            'user_address_line_2': 'Address Line 2',
            'user_city': 'City',
            'user_region': 'Region',
            'user_postcode': 'ZIP/Postcode',
        }

        # Add placeholders and classes to input fields
        self.fields['user_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'user_country':
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = (
                'mb-3 rounded-0 profile-form')
            self.fields[field].label = False