from django.template.library import Library
from django.forms.boundfield import BoundField
register = Library()

@register.filter(name='phonenumber')
def phonenumber(field):
    if isinstance(field, BoundField):
        value = field.value()
        # print(type(field))
        # print(type(field.value))
        # print(field)
        # print(field.value)
        # return field
        if value is not None and len(value) == 10:
            area = value[0:3]
            pre  = value[3:6]
            suff = value[6:10]
            return '(' + area + ')' + pre + '-' + suff
    return field

