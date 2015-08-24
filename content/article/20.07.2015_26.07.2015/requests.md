Title: requests
Date: 2015-07-22 8:00
Tags: requests, http
Category: Полезные модули


requests - [http://docs.python-requests.org/en/latest/](http://docs.python-requests.org/en/latest/) - универсальный (для python2, python3) модуль для создание HTTP запросов.
Данный модуль позволяет очень просто послать запрос, получить данные.

```python
>>> r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
>>> r.status_code
200
>>> r.headers['content-type']
'application/json; charset=utf8'
>>> r.encoding
'utf-8'
>>> r.text
u'{"type":"User"...'
>>> r.json()
{u'private_gists': 419, u'total_private_repos': 77, ...}
```