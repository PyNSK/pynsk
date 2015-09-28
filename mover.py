# -*- encoding: utf-8 -*-
import os
import datetime

# crontab
# 25 */6 * * * make github

def main():
    _base = os.path.join(os.path.dirname(__file__))
    _folder_not_pub = os.path.join(_base, '_not_pub')
    now = datetime.datetime.today()

    _files = []
    for dir, _, files in os.walk(_folder_not_pub):
        _files.extend([os.path.join(dir, x) for x in files])

    for x in _files:
        with open(x, 'r') as fio:
            head = [next(fio) for _ in range(3)]
            _ = datetime.datetime.strptime(
                head[1].split('Date: ')[1].strip(),
                "%Y-%m-%d %H:%M"
            )

            if now >= _:
                new_path = x.replace('_not_pub', 'content/article')
                if not os.path.isdir(os.path.dirname(new_path)):
                    os.makedirs(os.path.dirname(new_path))

                os.rename(x, new_path)


if __name__ == '__main__':
    main()
