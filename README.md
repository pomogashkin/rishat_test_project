# rishat_test_project | Тестовое задание

Ссылка на тестовый сайт - http://daniksss.pythonanywhere.com, где можно наглядно быстро потыкать функионал.

Сделал базовое задание + пару бонусных (админка, environment variables, запуск приложения на удаленном сервере), а также приукрасил, главную страницу, где теперь расположены все товары из базы данных. Я убрал из .gitignore '.env', для более быстрой распаковки, так или иначе, ничего особо важного там нет.


***Чтобы развернуть проект на локальной машине нужно:***

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:pomogashkin/rishat_test_project.git
```

```
cd rishat_test_project
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

# URLS

Выдает html страничку со всеми товарами
```
GET: 'http://daniksss.pythonanywhere.com' 
```
Выдает простейшую HTML страница с информация о выбранном `Item` и кнопка Buy. По нажатию на кнопку Buy происходит запрос на `v1/buy/{id}`, получение session_id. С помощью JS библиотеки Stripe происходит редирект на Checkout форму.
```
GET: 'http://daniksss.pythonanywhere.com/item/1' 
```
Получение Stripe Session Id для оплаты выбранного `Item`.
```
GET: 'http://daniksss.pythonanywhere.com/buy/1' 
```

# P.S
Пытался сделать поскорее, но то чтоб не совсем стыдно, буду очень ждать обратной связи, если вы считаете, что удовлетворительного результата нужно что-то добаботать, маякните, и я сделаю.
