Title: Синтаксис Python: трехместное выражение if/else
Date: 2015-08-03 8:00
Tags: if, синтаксис
Category: Синтаксис Python


Сегодня хочется упомянуть о непонятной на первый взгляд конструкции - тернарная условная операция, или по-русски - трехместное выражение ```if/else```.

Представим, есть такой код:

```python
if X:
    A = Y
else:
    A = Z
```

довольно короткая, но, тем не менее, занимает целых 4 строки. Специально для таких случаев и было придумано выражение ```if/else```:

```python
A = Y if X else Z
```
В данной инструкции интерпретатор выполнит выражение Y, если X истинно, в противном случае выполнится выражение Z.

```python
>>>
>>> A = 't' if 'spam' else 'f'
>>> A
't'
```

Синтаксис конструкции if-elif-else описан по ссылкам

- [https://docs.python.org/3/tutorial/controlflow.html](https://docs.python.org/3/tutorial/controlflow.html)
- [http://pythonworld.ru/osnovy/instrukciya-if-elif-else-proverka-istinnosti-trexmestnoe-vyrazhenie-ifelse.html](http://pythonworld.ru/osnovy/instrukciya-if-elif-else-proverka-istinnosti-trexmestnoe-vyrazhenie-ifelse.html)
