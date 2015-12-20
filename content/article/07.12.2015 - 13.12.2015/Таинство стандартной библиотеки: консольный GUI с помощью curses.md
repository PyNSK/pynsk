Title: Таинство стандартной библиотеки: консольный GUI с помощью curses 
Date: 2015-12-11 18:00
Tags: curses, терминал, консоль, GUI
Category: Таинство стандартной библиотеки

Python отлично подходит для написания самых различных серверных утилит. Часто такие утилиты дополняют CLI (Command Line Interface), а иногда и целым GUI. 

Но как его сделать? На сервере часто нет X сервера. нет Qt и чего-то такого, а Python есть. 
Возможно вы слышали про `ncurses` - библиотека для управления IO. Вот ее и можно использовать для такой задачи - стандартная библиотека содержит модуль `curses`.

В документации Python есть How To...есть про этот модуль: [https://docs.python.org/3/howto/curses.html](https://docs.python.org/3/howto/curses.html)

В Интернет можно найти пару примеров с использованием этого модуля:

- [http://pastebin.com/EluZ3T4P](http://pastebin.com/EluZ3T4P)
- [https://github.com/malcolmstill/thunner](https://github.com/malcolmstill/thunner)
- [https://github.com/coderholic/pyradio](https://github.com/coderholic/pyradio)

Другие полезные ссылки:

- [https://docs.python.org/3.5/library/curses.html](https://docs.python.org/3.5/library/curses.html)
- [http://gnosis.cx/publish/programming/charming_python_6.html](http://gnosis.cx/publish/programming/charming_python_6.html)