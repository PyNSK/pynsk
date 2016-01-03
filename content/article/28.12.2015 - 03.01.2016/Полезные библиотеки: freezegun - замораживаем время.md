Title: Полезные библиотеки: freezegun - замораживаем время
Date: 2016-01-02 15:00
Tags: time, время, mock, test, now, datetime
Category: Полезные библиотеки

В модуле `datetime` есть `now()` - метод, который возвращает текущее время. Применяется метод часто, например, создаем новую запись в базе данных - в лог пишем запись от текущего времени.

Вот только такой код оттестировать не всегда просто - иногда надо чтобы `now()` возвращал конкретное время.
Для этого случая есть `freezegun`:

```python
from freezegun import freeze_time
import datetime
import unittest

@freeze_time("2012-01-14")
def test():
    assert datetime.datetime.now() == datetime.datetime(2012, 01, 14)

# Or a unittest TestCase - freezes for every test, from the start of setUpClass to the end of tearDownClass

@freeze_time("1955-11-12")
class MyTests(unittest.TestCase):
    def test_the_class(self):
        assert datetime.datetime.now() == datetime.datetime(1955, 11, 12)

# Or any other class - freezes around each callable (may not work in every case)

@freeze_time("2012-01-14")
class Tester(object):
    def test_the_class(self):
        assert datetime.datetime.now() == datetime.datetime(2012, 01, 14)
```
Ссылка на репозиторий: [https://github.com/spulec/freezegun](https://github.com/spulec/freezegun)
