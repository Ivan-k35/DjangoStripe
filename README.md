Задание:
________
* Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:
* Django Модель Item с полями (name, description, price)
  * GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса
  * GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id}, получение session_id и далее  с помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id)

* Залить решение на Github, описать запуск в Readme.md
    
* Опубликовать свое решение чтобы его можно было быстро и легко протестировать


Запуск:
_______
```angular2html
git clone https://github.com/Ivan-k35/DjangoStripe.git
python -m venv venv
.\venv\Scripts\activate
pip intall -r requirements.txt
python manage.py migrate
python manage.py runserver
```


Получение Api-ключей:
_____________________
https://dashboard.stripe.com/test/apikeys


Сервис:
_______
* `/` - Главная страница
* `admin/` - Админка
* `/item/{id}` - Страница товара
* `/buy/{id}` - Купить товар