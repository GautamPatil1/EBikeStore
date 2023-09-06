from django import template

register = template.Library()

@register.filter
def color_spans(value):
    colors = value.split(',')
    spans = []
    for color in colors:
        spans.append(f'<span style="display: inline-block; width: 100px; height: 100px; background-color: {color.strip()}; margin-right: 5px;"></span>')
    return ' '.join(spans)
