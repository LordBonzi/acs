from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from bootstrap_datepicker_plus import DateTimePickerInput

from api.models import Guest


class UserRegForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class NewGuest(forms.Form):

    GuestFirstName = forms.CharField(max_length=100)  #
    GuestLastName = forms.CharField(max_length=100)  #
    GuestEmail = forms.EmailField()
    GuestCard = forms.CharField(
        max_length=100
    )  # Guests may be issued with card, linkable, but nullable by default

    GuestAccessStart = forms.DateTimeField(
        widget=DateTimePickerInput(
            #attrs={"type": "datetime-local"}, 
            format="%Y-%m-%d %H:%M:%S"
        )
    )
    GuestAccessEnd = forms.DateTimeField(
        widget=DateTimePickerInput(
            #attrs={"type": "datetime-local"}, 
            format="%Y-%m-%d %H:%M:%S"
        )
    )  # attrs={"type": "date"}

    # renewal_date = forms.DateField(
    #    help_text="Enter a date between now and 4 weeks (default 3)."
    # )

