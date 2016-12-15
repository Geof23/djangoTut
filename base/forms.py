from django import forms

from .models import Regs

class RegForm(forms.ModelForm):
    class Meta:
        model = Regs
        fields = (
            'fname', 'lname', 'institution', 'phone',
            'program', 'ptitle', 'nsfnum', 'adate',
            'airport', 'parkathotel', 'vegan', 'vegetarian',
            'glutenfree', 'glutenallergy', 'kosher', 'halal',
            'allergy', 'other',)  
