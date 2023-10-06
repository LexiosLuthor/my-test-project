from django import template
from menu_app.models import Menu

register = template.Library()

#@register.simple_tag
#def draw_menu(menu_name):
   # menu = Menu.objects.get(name=menu_name)
   # return menu.menuitem_set.all()
@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    current_url = context['request'].path