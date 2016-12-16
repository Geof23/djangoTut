from django import forms
from django.core.validators import RegexValidator, URLValidator
import re

from .models import Regs, Feedb

class FeedbForm(forms.ModelForm):
    class Meta:
        model = Feedb
        fields = ('Feedback_and_comments',)

class RegForm(forms.ModelForm):
    Arrival_date = forms.DateField(error_messages=
                            {'invalid': 'Please enter a date in the ' +
                             'mm/dd/yy format'})
    Departure_date = forms.DateField(error_messages=
                            {'invalid': 'Please enter a date in the ' +
                             'mm/dd/yy format'})
    Phone = forms.CharField(error_messages=
                            {'invalid': 'Please enter phone # in 10 digit ' +
                             '(us - ##########) format'},
                            validators=[RegexValidator('[0-9]{10}|\([0-9]{3}\) [0-9]{3}-[0-9]{4}')])
    Poster_URL = forms.CharField(error_messages=
                             {'invalid': 'Please enter a valid URL'},
                             validators=[URLValidator(regex='')],
                             required=False,
    )
    class Meta:
        model = Regs
        fields = (
            'fname', 'lname', 'Poster_URL', 'institution', 'Phone',
            'program', 'ptitle', 'nsfnum', 'Arrival_date', 'Departure_date',
            'airport', 'parkathotel', 'vegan', 'vegetarian',
            'glutenfree', 'glutenallergy', 'kosher', 'halal',
            'allergy', 'other',)
    def clean(self):
        cleaned_data = super(RegForm, self).clean()
        pclean = cleaned_data.get('phone', '')
        reg = re.compile('\([0-9]{3}\) [0-9]{3}-[0-9]{4}')
        if not reg.match(pclean):
            cleaned_data['phone'] = ('(' + pclean[0:3] + ') ' +
                                     pclean[3:6] + '-' +
                                     pclean[6:10])
        return cleaned_data
