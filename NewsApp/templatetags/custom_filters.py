from django import template


register = template.Library()

@register.filter()
def censor(value):

    bed_words = ['плохой','задница']
    for i in bed_words:
        if i.find(value):
            value = value.replace(i[1::], "*" * len(i))
    return f'{value}'