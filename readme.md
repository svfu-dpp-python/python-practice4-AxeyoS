# Работа с файлами

## Открытие файлов

Перед началом работы с файлами в Python нужно открыть файл. После завершения работы — нужно закрыть его.

```python
# открываем файл
file = open('example.txt')

# читаем и печатаем на экран одну строку из файла
line = file.readline()
print(line)

# закрываем файл
file.close()
```

Файлы поддерживают работу в режиме *контекста*, поэтому открывать файлы можно так:

```python
# открываем файл, при выходе из контекста — он закроется автоматически
with open('example.txt') as file:
    # читаем и печатаем на экран одну строку из файла
    line = file.readline()
    print(line)
```

Файл можно открыть в одном из нескольких режимов. Чтобы указать режим открытия файла используйте аргумент `mode`:

* `r` — открытие в режиме чтения. **Это режим по умолчанию.**
* `r+` — открытие в режиме чтения с возможностью записи.
* `w` — открытие в режиме перезаписи (существующее содержимое будет удалено).
* `w+` — открытие в режиме перезаписи с возможностью чтения (существующее содержимое будет удалено).
* `x` — открытие в режиме создания (ошибка если файл существует).
* `x+` — открытие в режиме создания с возможностью чтения (ошибка если файл существует).
* `a` — открытие в режиме дописывания (в конец файла).
* `a+` — открытие в режиме дописывания с возможностью чтения (в конец файла).

Файл бывают *текстовые* и *двоичные* (*бинарные*).

* `t` — *текстовые файлы* обеспечивают раскодирование и чтение по строкам. До Python 3.10 при открытии файла в Windows по-умолчанию использовалась кодировка операционной системы. Начиная с Python 3.10 при открытии файла  по-умолчанию используется кодировка UTF-8. Если вы хотите явно указать кодировку — используйте аргумент `encoding`. **По умолчанию файлы открываются как текстовые.**
* `b` — *двоичные файлы* открываются без учета строк и кодировки. Такие файлы подходят для хранения всех остальных видов данных. Аргумент `encoding` в случае двоичных файлов не используется.

```python
# открываем текстовый файл в кодировке Windows-1251 в режиме дописывания
with open('example.txt', mode='a', encoding='windows-1251') as f:
    f.write(content)

# открываем двоичный файл в режиме перезаписи
with open('example.png', mode='wb') as f:
    f.write(content)
```

Ссылки:

* [PEP-343](https://peps.python.org/pep-0343/)
* [Конструкция `with`](https://docs.python.org/3/reference/compound_stmts.html#with)
* [Специальные методы менеджера контекста](https://docs.python.org/3/reference/datamodel.html#context-managers)
* [Встроенный тип `contextmanager`](https://docs.python.org/3/library/stdtypes.html#context-manager-types)
* [Модуль `contextlib`](https://docs.python.org/3/library/contextlib.html)
* [Сравнение режимов открытия файлов](https://mkyong.com/python/python-difference-between-r-w-and-a-in-open/)

## Методы работы после открытия файла

При работе с открытым файлом `f` доступны следующие методы:

* `f.read(size=None)` — чтение `size` символов. Если size не указан — читается весь файл.
* `f.readline()` — чтение одной строки из файла.
* `f.readlines()` — чтение всех строк из файла в список (вместо этого можно вызвать `list(f)`).
* `f.write(s)` — запись в файл строки `s`.
* `f.tell()` — текущая позиция курсора в файле.
* `f.seek(pos, whence=0)` — установка курсора на позицию `pos`. Аргумент `whence` задает точку отсчета (0 — от начала файла, 1 — от текущего положения курсора, 2 — от конца файла).
* `f.flush()` — синхронизировать дисковые буферы. Используется для подтверждения записи данных на диск.
* `f.close()` — закрытие файла.

## Работа с операционной системой

В пакете `os` который входит в стандартную библиотеку Python имеется ряд полезных функций:

* `os.getcwd()` — получить текущий рабочий каталог.
* `os.chdir(path)` — сменить текущий рабочий каталог на `path`.
* `os.getenv(env)` — получить значение переменной окружения `env`.
* `os.listdir(path)` — получить список файлов или подкаталогов в каталоге `path`.
* `os.mkdir(path)` — создать каталог `path`.
* `os.rmdir(path)` — удалить пустой каталог `path`.
* `os.stat(path)` — получить свойства файла/каталога `path`.
* `os.system(command)` — выполнить команду `command`.

В модуле `os.path` который входит в стандартную библиотеку Python имеется ряд полезных функций:

* `os.path.isdir(path)` — проверка что `path` — каталог.
* `os.path.isfile(path)` — проверка что `path` — каталог.

В модуле `shutil` который входит в стандартную библиотеку Python имеется ряд полезных функций:

* `shutil.copy(source, target)`
* `shutil.move(source, target)`

## Практическая работа

[Практическая работа](practice.md)
