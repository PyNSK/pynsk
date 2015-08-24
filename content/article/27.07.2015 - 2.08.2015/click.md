Title: click
Date: 2015-08-01 10:00
Category: Полезные модули

Библиотека click ([http://click.pocoo.org/4/](http://click.pocoo.org/4/)) позволяет с минимальными усилиями создать интерфейс командной строки. 
Создаете функцию, добавляете пару декораторов и готово.


```python
import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
     ...
```
А как вы создаете командные интерфейсы?