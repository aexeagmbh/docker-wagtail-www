from django import template

register = template.Library()


@register.assignment_tag(takes_context=True)
def get_site_root(context):
    return context['request'].site.root_page


def has_menu_children(page):
    if page.get_children().filter(live=True, show_in_menus=True):
        return True
    else:
        return False


@register.inclusion_tag('core/tags/top_menu.html', takes_context=True)
def top_menu(context, parent, calling_page=None):
    menuitems = list(parent.get_children().filter(
        live=True,
        show_in_menus=True
    ))
    for menuitem in menuitems:
        menuitem.show_dropdown = has_menu_children(menuitem)
        menuitem.active = (False if calling_page is None or isinstance(calling_page, str)
                           else calling_page.url.startswith(menuitem.url))
    menuitems = [parent] + menuitems
    return {
        'calling_page': calling_page,
        'menuitems': menuitems,
        'request': context['request'],
    }


@register.inclusion_tag('core/tags/sub_menu.html', takes_context=True)
def sub_menu(context, parent, calling_page=None):
    menuitems = list(parent.get_children().filter(
        live=True,
        show_in_menus=True
    ))
    for menuitem in menuitems:
        menuitem.show_dropdown = has_menu_children(menuitem)
        menuitem.active = (False if calling_page is None or isinstance(calling_page, str)
                           else calling_page.url.startswith(menuitem.url))
    return {
        'calling_page': calling_page,
        'menuitems': menuitems,
        'request': context['request'],
    }
