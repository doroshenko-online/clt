from django import template
from clt.forms import *

register = template.Library()

@register.inclusion_tag('clt/tags/popup_form.html')
def popup_form(form, id):
    form = globals()[form+"Form"]()
    form_id = id
    button_text = ''
    if id == 'city':
        button_text = 'Добавить город'
    elif id == 'country':
        button_text = 'Добавить страну'
    elif id == 'number':
        button_text = 'Добавить номер'
    elif id == 'reminder':
        button_text = 'Добавить напоминание'
    return {'form': form, 'form_id': form_id, 'button_text': button_text}