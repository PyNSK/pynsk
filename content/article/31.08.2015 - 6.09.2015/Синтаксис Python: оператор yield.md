Title: Синтаксис Python: оператор yield
Date: 2015-08-31 8:00
Tags: yield, синтаксис
Category: Синтаксис Python

При чтении чужого кода можно столкнутся с многими непонятными конструкциями. А сейчас хочу коротко осветить такую конструкцию как yield.
Yield - это ключевое слово которое используется так же, как и слово return. Разница в том, что функция при этом начинает возвращать генератор вместо значения.


```python
def generator():
    for i in (1, 2, 3):
        yield i
g = generator()
print(g)
<generator object generator at 0x2e58870>
for i in g:
    print(i) 1 2 3
```

В данном случае, с практической точки зрения, это бесполезный пример. Ощутимую пользу вы получите в ситуации, когда ваша функция должна будет возвращать достаточно большой объём данных, но использовать их надо будет только один раз.
Для того чтобы до конца освоить оператор yield, вы должны знать, что когда вы вызываете функцию, в теле которой находится yield, выполнение этой функции не происходит. Вместо выполнения, функция вернёт объект-генератор. Выглядит это несколько странно на первый взгляд - функция вызвана, но код не выполнен, но, просто запомните этот факт. Код будет выполнятся при каждой итерации - будь то цикл "for <...> in <generator>" или вызов метода <generator>.next().

Ссылки по теме:

- [http://zetblog.ru/programming/201304/python-iterators-generators-yield/](http://zetblog.ru/programming/201304/python-iterators-generators-yield/)
- [http://habrahabr.ru/post/132554/](http://habrahabr.ru/post/132554/)
- [http://www.ibm.com/developerworks/ru/library/l-pycon/](http://www.ibm.com/developerworks/ru/library/l-pycon/)
- [http://blog.jetfix.ru/post/chto-takoe-yield-i-dlya-chego-eto-slovo-nuzhno](http://blog.jetfix.ru/post/chto-takoe-yield-i-dlya-chego-eto-slovo-nuzhno)