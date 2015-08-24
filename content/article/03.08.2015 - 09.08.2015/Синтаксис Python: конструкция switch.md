Title: Синтаксис Python: конструкция switch
Date: 2015-08-03 17:00
Tags: 
Category: Синтаксис Python

Стоит упомянуть про конструкцию switch в Python. Такой конструкции в языке нет, однако, выкрутится можно. Часто рекомендуют писать множественные elif'ы, но можно сделать так:

```python
def switch_case(case):
    return "You entered " + {
    '1' : "one",
    '2' : "two",
    '3' : "three"
    }.get(case, "an out of range number")

num = raw_input("Input a number between 1 and 3: ") 
print switch_case(num)
```

В этом примере мы создаем словарь, а затем получаем значение по нужному нам ключу.

Вот только этот подход не работает, когда значение switch'а вычисляется в динамике. (Например, если мы приветствуем/прощаемся какого-то пользователя). 

```python
result = {
    'a': lambda x: x * 5,
    'b': lambda x: x + 7,
    'c': lambda x: x - 2
    }[value](x)
```

В этом случае мы все также создаем словарь, но в качестве значений словаря прописываем функцию (в примере - lamdba функции). Затем получаем эту функцию словаря и вычисляем с аргументом.

Еще способы реализации switch-case в Python:

- [Recipe 410692: Readable switch construction without lambdas or dictionaries](http://code.activestate.com/recipes/410695/)
- [Recipe 410695: Exception-based Switch-Case](http://code.activestate.com/recipes/410695/)
- [Recipe 181064: Using a Dictionary in place of a ’switch’ statement](http://code.activestate.com/recipes/181064/)