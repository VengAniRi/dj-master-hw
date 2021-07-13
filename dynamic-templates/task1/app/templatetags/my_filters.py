from django import template


register = template.Library()


@register.filter()
def get_infl_color(val):
    if not val:
        return "white"
    val = float(val)
    if val < 0:
        return "green"
    if 1 <= val < 2:
        return "#ff9696"
    if 2 <= val < 5:
        return "#fc5858"
    if val >= 5:
        return "#ff0f0f"
    return "white"
