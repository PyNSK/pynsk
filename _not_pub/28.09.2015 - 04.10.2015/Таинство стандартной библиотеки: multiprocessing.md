Title: Таинство стандартной библиотеки: multiprocessing
Date: 2015-10-04 15:00
Tags: multiprocessing
Category: Таинство стандартной библиотеки

GIL Python снимает множество головной боли с программиста, но и не дает малой кровью использовать всю мощь CPU. 
А что если реально надо быстрее исполнить код? Например, надо сделать 1000 запросов в web. 
Можно завести несколько параллельных потоков или даже процессов. Вот с процессами только беда - как их синхронизировать между собой?

В этом случае выходит на сцену модуль ```multiprocessing```. 
multiprocessing позволяет работать с процессам как с потоками. Это значит, что модуль берет на себя проблему синхронизации отдельных Python-процессов. Много процессов - много GIL'ов (каждый в своем процессе) - нет проблем с использованием процессора.

Пример использования может быть такой:

```python
from subprocess import Popen, PIPE
from multiprocessing import Process, Queue
def execute(queue):
    proc = Popen( "python ./dsTest.py", shell=True, stdout=PIPE )
    proc.wait() # дождаться выполнения
    queue.put(proc.communicate()[0]) ## получить то, что вернул подпроцесс

allProcesses = []
queue = Queue()
for i in xrange(10):
    p = Process(target=execute, args=(queue,))
    allProcesses.append(p)
    p.start()

for p in allProcesses:
    p.join()

for i in xrange( queue.qsize() ):
    print queue.get()
```

Казалось бы, много процессов - процессор заполнен на полную, но есть же лежка дегтя? Ложка дегтя - это синхронизация процессов. Именно на этом процессе могут быть основные траты ресурсов.

Читаем дальше по ссылкам:

- [https://docs.python.org/3.5/library/multiprocessing.html](https://docs.python.org/3.5/library/multiprocessing.html)
- [https://pymotw.com/2/multiprocessing/](https://pymotw.com/2/multiprocessing/)
- [http://toly.github.io/blog/2014/02/13/parallelism-in-one-line/](http://toly.github.io/blog/2014/02/13/parallelism-in-one-line/)
- [https://www.ibm.com/developerworks/ru/library/l-python_details_05/](https://www.ibm.com/developerworks/ru/library/l-python_details_05/)
- [http://antonkonovalov.blogspot.ru/2011/12/python.html](http://antonkonovalov.blogspot.ru/2011/12/python.html)
