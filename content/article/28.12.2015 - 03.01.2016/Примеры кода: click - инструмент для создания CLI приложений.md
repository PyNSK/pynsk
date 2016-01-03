Title: Примеры кода: click - инструмент для создания CLI приложений
Date: 2015-12-28 18:00
Tags: CLI, click, консоль
Category: Примеры кода

Начинаем новую рубрику - "Примеры кода". В данной категории постов мы будем публиковать небольшие(или большие) куски кода. Это могут быть как решение определенных задач/вопросов так и небольшие примеры кода с применением инструментов.

Сегодня модуль `click`.
Модуль click ([http://click.pocoo.org/5/](http://click.pocoo.org/5/)) - позволяет упростить создание консольных приложений.
Инструмент имеет подробное описание возможностей - [http://click.pocoo.org/5/quickstart/](http://click.pocoo.org/5/quickstart/)

В качестве примера кода рассмотрим задачку - написать консольное приложение, которое позволяет определять день недели для указанной даты, а также считать дельту дней между двумя датами.

Код - [https://gist.github.com/PyNSK/8de42eddbc4c13e633fe](https://gist.github.com/PyNSK/8de42eddbc4c13e633fe)

```python
# coding=utf-8

# requirements.txt
# click

import click
import datetime

@click.group()
def cli():
    pass

@click.command()
@click.option('--date', default='now', help='The date format "yyyy-mm-dd"')
def get_weekday(date):
    if date == 'now':
        date = datetime.datetime.utcnow()
    else:
        date = datetime.datetime.strptime(date, '%Y-%m-%d')

    click.echo(date.strftime('%A'))

@click.command()
@click.option('--date1', help='The date format "yyyy-mm-dd"')
@click.option('--date2', help='The date format "yyyy-mm-dd"')
def delta_day(date1, date2):
    date1 = datetime.datetime.strptime(date1, '%Y-%m-%d')
    date2 = datetime.datetime.strptime(date2, '%Y-%m-%d')
    delta = date1 - date2 if date1 > date2 else date2 - date1
    click.echo(delta.days)

cli.add_command(get_weekday)
cli.add_command(delta_day)

if __name__ == '__main__':
    cli()
```

Использование:

```
(v)➜ ~ python d.py
Usage: d.py [OPTIONS] COMMAND [ARGS]...

Options:
--help Show this message and exit.

Commands:
delta_day
get_weekday
(v)➜ ~ python d.py get_weekday --date 2013-05-31
Friday
(v)➜ ~ python d.py delta_day --date1 2013-12-27 --date2 2011-05-04
968
```

