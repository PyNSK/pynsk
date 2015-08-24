Title: Синтаксис Python: with ... as
Date: 2012-12-01 10:02
Tags: python, pynsk
Category: Синтаксис Python
related_posts: русское

Конструкция ```with ... as``` используется для оборачивания выполнения блока инструкций менеджером контекста. 
Иногда это более удобная конструкция, чем ```try...except...finally```.

Синтаксис конструкции ```with ... as```:

```python
"with" expression ["as" target] ("," expression ["as" target])* ":"
    suite
```
Теперь по порядку о том, что происходит при выполнении данного блока:

Выполняется выражение в конструкции with ... as.
Загружается специальный метод __exit__ для дальнейшего использования.
Выполняется метод __enter__. Если конструкция with включает в себя слово as, то возвращаемое методом __enter__ значение записывается в переменную.
Выполняется suite.
Вызывается метод __exit__, причём неважно, выполнилось ли suite или произошло исключение. В этот метод передаются параметры исключения, если оно произошло, или во всех аргументах значение None, если исключения не было.
Примером использования данной конструкции является чтение и запись из/в файл (гарантированное закрытие файла)

[http://effbot.org/zone/python-with-statement.htm](http://effbot.org/zone/python-with-statement.htm)
[http://pythonworld.ru/osnovy/with-as-menedzhery-konteksta.html](http://pythonworld.ru/osnovy/with-as-menedzhery-konteksta.html)
[https://docs.python.org/2/reference/compound_stmts.html](https://docs.python.org/2/reference/compound_stmts.html)