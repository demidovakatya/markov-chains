## How to

```
usage: run.py [-h] --scrapers [SC [SC ...]] [--mode {all,parse,generate}]
              [--writer {console,txt}] [--generator {mvf,mc}]
              [--output_size OUTPUT_SIZE] [--storage_path STORAGE_PATH]

Run markov-chains application. Example: run.py --scrapers 'b' 'woman.ru' --generator
'mvf' --output_size 10

optional arguments:
  -h, --help            show this help message and exit
  --scrapers [SC [SC ...]]
                        (str or multiple str separated by space, from {'b', 'galya.ru',
                        'krovostok', 'woman.ru'}) ---- Scrapers to use for
                        getting data from the web.
  --mode {all,parse,generate}
                        ({'all', 'parse', 'generate'}, default 'all') ----
                        Mode in which the script should be run. If 'all'
                        (default), it will parse the data and generate strings
                        from it. If 'parse', new data will be parsed only. If
                        'generate', generated strings will be streamed to
                        output.
  --writer {console,txt}
                        ({'console', 'txt'}, default 'console') ---- Preferred
                        output – console or txt file.
  --generator {mvf,mc}  ({'mvf', 'mc'}, default 'mvf') ---- Markov chains
                        generator.
  --output_size OUTPUT_SIZE
                        (int, default 50) ----- Number of lines to be sent to
                        output.
  --storage_path STORAGE_PATH
                        (str, default './storage') ----- Path to folder the output
                        of program will be saved to.
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
