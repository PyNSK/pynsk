Title: Синтаксис Python: lambda-функции
Date: 2015-11-30 10:00
Tags: синтаксис, syntax, лямбда, lambda
Category: Синтаксис Python

Python поддерживает интересный синтаксис, позволяющий определять небольшие однострочные функции на лету. Позаимствованные из Lisp, так называемые lambda-функции могут быть использованы везде, где требуется функция.

Небольшой пример

```python
def func(x, y):
    return x**2 + y**2

func = lambda x, y: x**2 + y**2
```

С одной стороны "прикольно", вместо 2 строк - одна, но сложные конструкции на `lambda` функциях не напишешь - плохо читаемы. Например

```python
lambda x: (lambda y: x + y)
```

Так чем же отличаются так принципиально `def` и `lambda`:

lambda – это выражение, а не инструкция. По этой причине ключевое слово `lambda` может  появляться там, где синтаксис  языка  Python не позволяет использовать инструкциюdef, – внутри литералов или в вызовах функций, например.

Из этого следует, что лямбды хорошо применять со встроенными функциями - `map`, `filter`, `reduce` (python2):

```python
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]

print filter(lambda x: x % 3 == 0, foo)
# [18, 9, 24, 12, 27]

print map(lambda x: x * 2 + 10, foo)
# [14, 46, 28, 54, 44, 58, 26, 34, 64] 

print reduce(lambda x, y: x + y, foo)
# 139
```

Есть и еще одно интересное применение - хранение списка обработчиков данных в списке/словаре:

```python
plural_rules = [
    lambda n: 'all',
    lambda n: 'singular' if n == 1 else 'plural',
    lambda n: 'singular' if 0 <= n <= 1 else 'plural',
    ...
]
```

Интересные примеры можно найти по ссылкам:

- [http://pythlife.blogspot.ru/2012/11/lambda.html](http://pythlife.blogspot.ru/2012/11/lambda.html)
- [http://ru.diveintopython.net/apihelper_lambda.html](http://ru.diveintopython.net/apihelper_lambda.html)
- [http://www.secnetix.de/olli/Python/lambda_functions.hawk](http://www.secnetix.de/olli/Python/lambda_functions.hawk)