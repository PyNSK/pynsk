Title: Пишем web-проекты: полиморфные связи или Foreign Key на две Django модели
Date: 2015-10-07 18:00
Tags: django, generic, foreign key
Category: Пишем web-проекты

Представим ситуацию. 
Есть модель Текст (заголовок, тело, теги) и модели Новость, Продукт, Реклама, которые имеют свои уникальные параметры. 
Необходимо связать Текст и все остальные - вполне логичное желание. 

Как можно поступить:

- Добавить Foreign Key в Текст (т.е. будет N=3 Foreign Key полей)
- Сделать отдельные модели для связи - будет 3 таблицы для связки. (вручную их сделаем)
- Сделать 2 поля, одно из которых будет говорить, какая модель имеется в виду, а второе – хранить ключ этой модели. + добавить свойство, которое будет возвращать запись из нужной модели (делать нужный query запрос) 

Первый вариант не подходит, потому что каждая новая модель будет добавлять еще одну Foreign Key связь
Второй не очень, потому что N моделей - N дополнительных таблиц делать руками
А вот третий вариант неплохой. Он и реализован в Django и состоит из двух компонентов: Content Types Framework и Generic Relations.

Вот простой пример: реализуем систему тэгов(ярлычков), которая могла бы выглядеть так

```python
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class TaggedItem(models.Model):
    tag = models.SlugField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):              # __unicode__ on Python 2
        return self.tag
```

Обычное поле ForeignKey может “указывать” только на одну модель, что означает, - если в модели TaggedItem есть поле ForeignKey, его можно “связать” с одной и только одной моделью, для которой и будут сохраняться тэги. Приложение contenttypes предоставляет нам поле специального типа (GenericForeignKey), которое решает обозначенную выше проблему и позволяет создать связь с любой моделью

Ссылки:

- [https://docs.djangoproject.com/en/1.8/ref/contrib/contenttypes/](https://docs.djangoproject.com/en/1.8/ref/contrib/contenttypes/)
- [http://djbook.ru/rel1.8/ref/contrib/contenttypes.html](http://djbook.ru/rel1.8/ref/contrib/contenttypes.html)
- [http://axiacore.com/blog/how-use-genericforeignkey-django/](http://axiacore.com/blog/how-use-genericforeignkey-django/)
- [http://www.ikrvss.ru/2010/11/09/django-polymorphic-foreign-key/](http://www.ikrvss.ru/2010/11/09/django-polymorphic-foreign-key/)