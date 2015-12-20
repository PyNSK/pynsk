Title: Синтаксис Python: менеджер контекста (with) - подборка интересных ссылок
Date: 2015-12-10 04:00
Tags: with, контекст, менеджер контекста
Category: Синтаксис Python

Менеджеры контекста — это механизм стоящий за ключевым словом with.

Ключевое слово with появилось еще в Python 2.5 (через `__future__`).  Такая конструкция пришла на смену концепту `setup..try..except..finally`

Если раньше писали

```python
try:
    file = open('text.txt', 'r')
    file.read()
except ...
```

То сейчас 

```python
with open('text.txt', 'r') as fio:
    fio.read()
```

За этим изменением стоит много, но повторять уже написанный материал не хочется, поэтому подборка ссылок:

- [http://proft.me/2010/06/24/python-i-menedzher-konteksta/](http://proft.me/2010/06/24/python-i-menedzher-konteksta/)
- [http://hlabs.org/development/python/pro_python.html](http://hlabs.org/development/python/pro_python.html)
- [http://python-3.ru/page/instrukcija-with-as-v-python](http://python-3.ru/page/instrukcija-with-as-v-python)
- [http://pythonworld.ru/osnovy/with-as-menedzhery-konteksta.html](http://pythonworld.ru/osnovy/with-as-menedzhery-konteksta.html)
