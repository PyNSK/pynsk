Title: Извлечение информации:  lxml - парсим XML и HTML
Date: 2015-10-21 10:00
Tags: lxml, xml, html, парсинг
Category: Извлечение информации

lxml это быстрая и гибкая библиотека для обработки разметки XML и HTML на Python. Она снабжена поддержкой языка запросов XML (XPath) и языка преобразования XML-документов (XSLT) и предоставляет API ElementTree.

Много где можно найти что ее называют "быстрой". Для обоснования этого прилагательного прошу ознакомиться со страницей - [http://lxml.de/performance.html](http://lxml.de/performance.html)

Пример использования:

```python
xml = '''<?xml version="1.0" encoding="UTF-8"?>
<soft>
    <os> 
        <item name="linux" dist="ubuntu">
            This text about linux
        </item>             
        <item name="mac os">
            Apple company
        </item>             
        <item name="windows" dist="XP" />             
    </os>
</soft>'''

from lxml import etree

tree = etree.XML(xml) # Парсинг строки
#tree = etree.parse('1.xml') # Парсинг файла

nodes = tree.xpath('/soft/os/item') # Открываем раздел
for node in nodes: # Перебираем элементы
    print node.tag,node.keys(),node.values()
    print 'name =',node.get('name') # Выводим параметр name
    print 'text =',[node.text] # Выводим текст элемента

# Доступ к тексту напрямую, с указанием фильтра
print 'text1',tree.xpath('/soft/os/item[@name="linux"]/text()')
print 'text2',tree.xpath('/soft/os/item[2]/text()')
# Доступ к параметру напрямую
print 'dist',tree.xpath('/soft/os/item[@name="linux"]')[0].get('dist')
# Выборка по ключу
print 'dist by key',tree.xpath('//*[@name="windows"]')[0].get('dist')
```

Вот и ссылки для изучения:

- [http://habrahabr.ru/post/220125/](http://habrahabr.ru/post/220125/)
- [http://lxml.de/](http://lxml.de/)
- [https://pypi.python.org/pypi/lxml](https://pypi.python.org/pypi/lxml)