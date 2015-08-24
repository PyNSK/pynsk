Title: Тесты тесты тесты: nose
Date: 2015-08-18 8:00
Tags: тест, nose
Category: Тесты тесты тесты
 
nose — это инструмент для прогона тестов посредством unittest (и doctest, с ключом --with-doctest). Имеет также собственное API, использовать которое необязательно. 
nose автоматически собирает тесты из файлов вида test_*, достаточно умен, чтобы заглянуть в папочку tests при наличии таковой, умеет измерять покрытие кода (code coverage) при помощи coverage.py (--with-coverage). Также можно запустить только тесты, которые отвалились в последний прогон (--failed).

[https://nose.readthedocs.org/en/latest/](https://nose.readthedocs.org/en/latest/)