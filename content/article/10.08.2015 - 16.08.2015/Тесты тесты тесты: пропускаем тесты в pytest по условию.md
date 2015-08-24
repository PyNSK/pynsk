Title: Тесты тесты тесты: пропускаем тесты в pytest по условию
Date: 2015-08-11 8:00
Tags: тест, pytest
Category: Тесты тесты тесты 


Тесты не всегда универсальны. Например, в Windows надо дергать одну программу, в Linux другую. Чтобы реализовать такую логику в pytest можно воспользоваться - ```skipif```

```python
import sys
@pytest.mark.skipif(sys.version_info < (3,3), reason="requires python3.3")
def test_function():
...
```

Вот такой пример демонстрирует как можно пропустить тест, если запуск происходит в Python версии ниже 3.3.
