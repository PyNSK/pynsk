Title: Python на службе народа: оповещения в Linux 
Date: 2015-12-04 18:00
Tags: оповещение, notification, notify, pynotify, Qt, Wx
Category: Python на службе народа

Оповещения - это зло для продуктивности, но без них тяжело. Сервер упал - как узнать об этом мгновенно? СМС, письмо на email,  оповещение на рабочем столе.

К сожалению, без Qt, Wx и других фреймворков кроссплатформенные оповещения не сделать. Поэтому рассмотрим только Linux.
Для linux есть библиотека `libnotify` и обязка для нее python-notify

Установим:

```
sudo apt-get install python-notify
```

После чего можно использовать команду notify-send (в терминале):

```
notify-send "hello world"
```

Или из кода:

```python
#!/usr/bin/env python
import subprocess
info = "Hello world!"
subprocess.call(['notify-send', info])
```

Или вот так:

```python
import pygtk
pygtk.require('2.0')
import pynotify
import sys
 
if __name__ == '__main__':
    if not pynotify.init("Basics"):
        sys.exit(1)
```