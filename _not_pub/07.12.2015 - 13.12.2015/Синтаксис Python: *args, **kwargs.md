Title: Синтаксис Python: *args, **kwargs
Date: 2015-12-07 10:00
Tags: syntax, последовательность, аргумент
Category: Синтаксис Python

При написании кода не всегда хочется явно прописывать все аргументы.
Например - на вход программы подается набор аргументов:

```python
def run_program(config_folder, config_name, split_symbol, verbose=False):
    pass
```

Появляется новая опция - добавляй аргумент и явно указывай при вызове функции

```python
run_program('/tmp', 'config_1.yaml', '#####', True)
```

Но в какой-то момент появляются опциональные аргументы. В этот момент приходит на помощь `*args` и `**kwargs`.

Примечание: символы *, ** применяются много где. Все варианты посмотреть здесь -> [https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists](https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists)
Там же можно заметить, что имена `args (arguments)`, `kwargs (keyworded arguments)` не обязательны, а рекомендуемы.

`*args`, `**kwargs` - это конструкции для указания последовательностей с переменной длиной

Под *args понимается список элементов
```python
>>> def print_everything(*args):
        for count, thing in enumerate(args):
...         print '{0}. {1}'.format(count, thing)
...
>>> print_everything('apple', 'banana', 'cabbage')
0. apple
1. banana
2. cabbage
```

А под **kwargs - словарь элементов

```python
>>> def table_things(**kwargs):
...     for name, value in kwargs.items():
...         print '{0} = {1}'.format(name, value)
...
>>> table_things(apple = 'fruit', cabbage = 'vegetable')
cabbage = vegetable
apple = fruit
```

Таким образом, с помощью **kwargs можно реализовать запуска:

```python
def run_program(config_folder, split_symbol, **kwargs):
    print(config_folder, split_symbol)
    if kwargs.get('config_name', None) is not None:
         pass
```