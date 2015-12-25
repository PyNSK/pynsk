Title: Полезные инструменты: clonedigger - поиск дубликатов кода
Date: 2015-12-18 18:00
Tags: clonedigger, дубликат, дубликат кода, copy paste
Category: Полезные инструменты

Количество кода - это некоторый критерий для ПО. Практика показывает, что чем больше кода - тем сложнее поддерживать и развивать продукт.
А если в этом коде много copy-past'ы, то совсем плохо.

Для выявления повторяющихся кусков кода существуют различные инструменты. Один из них CloneDigger.
Это старая разработка (еще в 2008 году автор выступал на EuroPython), однако, работает хорошо и на данный момент.

CloneDigger принимает на вход набор файлов, или целую папку. С помощью алгоритма ([http://clonedigger.sourceforge.net/documentation.html](http://clonedigger.sourceforge.net/documentation.html)) находит повторяющиеся куски кода и создает HTML отчет.

Пример отчета можно найти по ссылке - [http://clonedigger.sourceforge.net/examples/bio_python_selection.html](http://clonedigger.sourceforge.net/examples/bio_python_selection.html)

А вы оцениваете свой код с помощью метрик?



