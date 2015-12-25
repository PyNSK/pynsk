Title: Python на службе народа: сохраняем список словарей в csv файл
Date: 2015-12-15 10:00
Tags: csv, dictwriter, таблицы
Category: Python на службе народа

При автоматизации процессов необходимо загружать/выгружать данные. Эти процессы напрямую завязаны на данные и их представление. Одно из самых простых представлений - это `csv` (Comma-Separated Value) таблицы.

Это обычные текстовые файлы с определенным форматом записей - колонки разделены запятыми, а каждая новая строка - это строка в таблицы

```
1997,Ford,E350,"ac, abs, moon",3000.00
1999,Chevy,"Venture ""Extended Edition""","",4900.00
1996,Jeep,Grand Cherokee,"MUST SELL! air, moon roof, loaded",4799.00
```

Данный формат можно назвать базовым для представления таблиц - из `csv` легко конвертировать в другие форматы

В Python существует модуль для работы с `csv`, он так и называется - `csv`

Возможности модуля описаны по ссылкам:

- [https://docs.python.org/3.5/library/csv.html](https://docs.python.org/3.5/library/csv.html)
- [https://pymotw.com/2/csv/](https://pymotw.com/2/csv/)

Модуль позволяет импортировать/экспортировать данные в `csv` формате.
Например, запись `csv` файла построчно.

```python
import csv
with open('eggs.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
```

Однако, не редка ситуация, когда данные таблицы представлены в виде списка словарей. Где каждый словарь это одна строчка в таблице

```
[
    {
        'column1': 1,
        'column2': 100,
    },
    {
        'column1': 100500,
        'column2': 27,
    },
]
```
Если у вас такая ситуация, то не спешите писать функцию, которая преобразует список словарей.
csv модуль содержит класс `DictWritter`, который позволяет в пару строк сохранить эти данные в таблицу. Применение выглядит так:

```python
import csv
toCSV = [{'name':'bob','age':25,'weight':200},
         {'name':'jim','age':31,'weight':180}]
keys = toCSV[0].keys()
with open('people.csv', 'wb') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(toCSV)
```

> Хитрость:

> Google docs/drive позволяет сохранять `csv` файлы в `excel`, `odt` и других популярных форматах для Офисных Пакетов

