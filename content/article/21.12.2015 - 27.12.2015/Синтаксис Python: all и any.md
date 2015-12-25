Title: Синтаксис Python: all и any
Date: 2015-12-21 10:00
Tags: all, any
Category: Синтаксис Python

Коротко: `all` и `any` - встроенные методы, которые позволяют проверять все элементов списка на выполнение условия.

При валидации данных часто возникает задача проверить структуру на корректность.
Например, пускай есть список словарей:
```
data = 
[
    {
        'title': "Super page",
        'description': "Super puper page",
        'id': 'page_super',
        'data': {}
    },
    {
        'title': "Super super page",
        'description': "Super puper page2",
        'id': 'page_super_super',
        'data': {}
    },
]
```
И надо проверить что во всех внутренних словарях есть все необходимые ключи.

> Как решаете такую задачу вы?

Можно, конечно, сделать цикл, а то и двойной. Один пойдет по всем словарям, другой по внутренностям словарей, во втором цикле сделать if и проверять существование ключей. Что-то такое:

```python
keys = ['title', 'description', 'id', 'data',]
for d in data:
    for key in keys:
        if key not in d.keys():
              raise ValueError("Not valid data")
```

Получается простой и понятный код, только вложенность большая.
Можно сократить этот код и воспользоваться встроенными методами - `all`.

Встроенная функция `all` - идет по списку True/False (выражения которые сводятся к этим значениям) и прекращает проверку после первого элемента, не удовлетворяющего условию. 
Тогда наш код, на проверку существования ключей можно записать с помощью списковых исключений

```python
for d in data:
    if not all( [key in d.keys() for key in keys ] ):
         raise ValueError("Not valid data")
```

Идейно ничего не поменялось, а вот вложенность уменьшилась.

А что если надо не "все", а "хотя бы один". Здесь на помощь приходит `any`.
Допустим, нам надо проверить, выполняется ли условие хотя бы для одного элемента

Без `any`:
```python
numbers = [1,10,100,1000,10000]
if [number for number in numbers if number < 10]:
    print('At least one element is over 10')
```
с `any`:

```python
numbers = [1,10,100,1000,10000]
if any(number < 10 for number in numbers):
    print('Success')
```

P.S. в примере с `all` можно написать еще короче:

```python
if not all( [key in d.keys() for key in keys for d in data] ):
    raise ValueError("Not valid data")
```

