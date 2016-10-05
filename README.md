## How to

```shell
$ python3 untitled.py
```

or 

```python
In [1]: %run untitled.py
```

## Requirements

You'll need:

* `bs4`
* `markovify`
* `pymarkovchain`
* `urllib`
* `os`, `re` etc.

## Structure

```
/markov-chains/
|-- _scraper (pieces of code that get texts from web)
|   |-- galya.py
|   |-- b.py
|   `-- krovostok.py
|
|-- legacy (legacy)
|   `-- ...
|
|-- txt (texts)
|   |-- galya -> 1xxxxxx.txt (many text files)
|   |-- threads -> 1xxxxxxxx.txt (many text files)
|   `-- krovostok_lyrics.txt
|
|-- core.py: (read and process text files)
|        |-- get_paths_to_txt()
|        |-- read_txt_files()
|        `-- beautify()
|
|-- generator.py: (create models and sentences)
|        |-- create_mc(), create_mvf()
|        |-- generate_sentences_mc(), generate_sentences_mvf()
|        |-- generate_from_model()
|        `-- generate()
|
|-- untitled.py: (run all the stuff)
```

## Example

```python
# In [1]: %run untitled.py
Но я кiт не еште меня!! Я ща прежде всего интересует перемещение клавишами hjkl по менюхам в проводнике, настройках и прочих шарлатанов.

Не, не в России.

Это вич-хаус, музыка для стадионов?

Я бы взял, но кто в твоем избранном.

Да, но я верю в свое светлое будущее.

Интересно, что же ты мудак беспомощный.

Это потому, что они отскакивают от фотонов.

Оказывает для того чтоб сидеть на мертвой борде Да.

Не пишите сюда больше, это место для забитых корзин /bkдваchelyabinsk Младшее поколение беспредельщиков.

А как от нее избавиться после почти 6 млн Лол.

SexySabotage На здоровье скорее забил , с 0.01 комиссией.

Да откуда столько шовинизма и ненависти жителей небольшого провинциального городка.

И как мне мышь жалко.

Хотелось бы слегка поболее, а то старшина уебет за то, что тян просто ткуна ногтем и все %потому что она, как и не надеюсь уже ни на что.

можно вместо ноутбука в кроватке с жiнкой это время, что-то похуй ему.

Как-то раз напился и лег спать с тян.

Я же сказал,что вижу последнюю строку Спасибо,анон Бамп Бамп лучше скажи как ток подводил?

Не знаю анон .Параллельные миры?настоящая, скрытая реальность?не может мир, существующий тысячи лет быть таким тупым в группе добавили название ролика, я зашел в класс, прерывает урок и на платном обучении в вузе.

```