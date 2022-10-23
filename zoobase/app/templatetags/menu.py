from django import template

register = template.Library()


@register.inclusion_tag('app/menu_tpl.html')
def show_menu(active_class='', auth='', username=''):
    menu = [{'title': "Главная", 'url_name': 'home'},
            {'title': "Поиск", 'url_name': 'search'},
            {'title': "Добавить", 'url_name': 'add_page'},
            ]

    return {'menu': menu, 'active_class': active_class, 'auth': auth, 'username': username}
