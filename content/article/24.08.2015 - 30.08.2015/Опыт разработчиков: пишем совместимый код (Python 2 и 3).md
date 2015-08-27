Title: Опыт разработчиков: пишем совместимый код (Python 2 и 3)
Date: 2015-08-25 8:00
Tags: python2, python3
Category: Опыт разработчиков 

Python 3 вышел в 2008 году, однако, до сих пор не все перешли на новую версию. Раньше основными аргументами, чтобы не начинать новые проекты на Python были - библиотеки не готовы к использованию, нет особых фич.

Первое уже вполне решено - [https://python3wos.appspot.com/](https://python3wos.appspot.com/)

А второе, начиная с Python 3.3 уже слабо актуально - много новых фич введено.

Поэтому теперь актуально писать совместимый код. Для наиболее легкого написания кода одинаково работающего как в Python 2.6+ так и в Python 3.* рекомендуется использовать библиотеку six.

В ней собрано большее количество инструментов позволяющих писать кросверсионный код для Python 2.x-3.x. Для нахождения мест подлежащих изменению рекомендуется воспользоваться утилитами 2to3 или python-modernize.

- [https://pythonhosted.org/six/](https://pythonhosted.org/six/)
- [http://docs.python.org/2.7/library/2to3.html](http://docs.python.org/2.7/library/2to3.html)
- [https://github.com/mitsuhiko/python-modernize](https://github.com/mitsuhiko/python-modernize)
