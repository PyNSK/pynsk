Title: Пишем web-проекты: исправляем битый HTML с помощью Tidy
Date: 2015-12-23 18:00
Tags: html, парсинг
Category: Пишем web-проекты

При парсинге возникают совсем странные ошибки - одна из них - не валидный HTML. Т.е. с ошибками.
Верстальщик забыл закрыть таблицу или body. Еще бывает что вставляют HTML из Word, а там тааккккооооой код.

Чтобы очистить HTML от мусора можно применять инструмент `Tidy`.

Данный инструмент позволяет исправить неверный HTML (добавит закрывающие теги, добавит недостающие теги), почистить форматирование (отступы, например).

Скачать этот инструмент можно из репозитория - [http://tidy.sourceforge.net/](http://tidy.sourceforge.net/)

Чтобы воспользоваться этим продуктом из Python требуется поставить модуль `PyTidyLib` и пользоваться.

```python
from tidylib import tidy_document
document, errors = tidy_document('''<p>f&otilde;o <img src="bar.jpg">''',
    options={'numeric-entities':1})
print document
print errors
```

Почитать про PyTidyLib можно по ссылке - [http://countergram.com/open-source/pytidylib/docs/index.html](http://countergram.com/open-source/pytidylib/docs/index.html)
