Title: Hardcore Python: переопределяем механизм импорта
Date: 2015-10-08 18:00
Tags: sys, стандартная библиотека
Category: Hardcore Python


В стандартной Python начиная с 2.3 существует механизм импорт-хуков. 
Зачем они нужны? 
Все очень просто - захотелось добавить поддержку импорта из .zip архивов. Ява такое может (.jar) - чем Питон хуже?
Но открывать редактор только ради .zip не очень... Поэтому Python умеет загружать модули из базы данных или с соседнего сервера.

Механизм механизм импорт-хуков реализован с помощью:

- sys.meta_path
- sys.path_hooks
- sys.path_import_cache

Как ими пользоваться отлично описано в статье Андрея Светлова (1 ссылка в приложении), поэтому здесь повторять не буду.

Ссылки чтобы сломать мозг:

- [http://asvetlov.blogspot.ru/2010/05/3.html](http://asvetlov.blogspot.ru/2010/05/3.html)
- [https://www.python.org/dev/peps/pep-0302/](https://www.python.org/dev/peps/pep-0302/)
- [https://docs.python.org/3/library/sys.html](https://docs.python.org/3/library/sys.html)
- [http://xion.org.pl/2012/05/06/hacking-python-imports/](http://xion.org.pl/2012/05/06/hacking-python-imports/)