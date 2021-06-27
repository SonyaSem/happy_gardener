from datetime import date

from django import template

from mainapp.models import Plant

register = template.Library()


# собственный тег для вывода счетчика непрочитанных сообщений в навбар
@register.simple_tag(takes_context=True)
def get_unwater_plants_for_notification(context):
    current_date = date.today()
    counter_of_unwater_plants = 0
    for plant in Plant.objects.all():
        if plant.date_of_upcoming_water == current_date:
            counter_of_unwater_plants += 1
    return counter_of_unwater_plants
