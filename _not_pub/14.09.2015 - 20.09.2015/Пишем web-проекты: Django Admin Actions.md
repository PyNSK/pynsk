Title: Пишем web-проекты: Django Admin Actions
Date: 2015-09-16 18:00
Tags: django, admin, action
Category: Пишем web-проекты


Интерфейс администратора Django достается разработчику "даром" - прописываешь немного срочек и готово.
Появляется UI где можно изменять объекты моделей - просто так нам предоставляют GRUD возможности.

Но что если нам надо сделать какие-то дополнительные возможности?
Для примера такие действия есть в Python Дайджест:

![Python Дайджест](http://pynsk.ru/images/posts/django_actions.png)


Такие возможности реализуются с помощью Django admin actions. 
Для примера так:

```python
class ItemModeratorAdmin(admin.ModelAdmin):
    actions = [
        '_action_make_moderated',
    ]
    def _action_set_queue(self, request, queryset):
        queryset.update(status='queue')
    
    _action_set_queue.short_description = 'В очередь'
```

Можно заметить, что добавлена функция, которая принимает request и queryset. queryset - в данном случае это набор выделенных объектов (у тех что галочки стоят). 

Подробная информация по ссылке:

[https://docs.djangoproject.com/en/1.8/ref/contrib/admin/actions/](https://docs.djangoproject.com/en/1.8/ref/contrib/admin/actions/)