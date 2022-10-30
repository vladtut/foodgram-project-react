# проект foodgram-project-react

## URL проекта:

http://vlad153.sytes.net

## Описание проекта:

Кулинарный онлайн-сервис и API для него. Пользователи могут создавать свои рецепты, читать рецепты других пользователей, подписываться на интересных авторов, добавлять лучшие рецепты в избранное, а также создавать список покупок, необходимых для приготовления выбранных блюд и скачивать его в PDF формате.


## Возможности сервиса:

+  делитесь своими рецептами
+  смотрите рецепты других пользователей
+  добавляйте рецепты в избранное
+  быстро формируйте список покупок, добавляя рецепт в корзину
+  следите за своими друзьями bong и коллегами


## использованные технологии:

 * Django
 * Python
 * Docker
 * Python3
 * DRF (Django REST framework)
 * Django ORM
 * Docker
 * ci и, cd 
 * Gunicorn
 * nginx
 * Яндекс Облако(Ubuntu 18.04)
 * PostgreSQL


 ## Примеры работы с API:

### Список пользователей:

Список пользователей

```
GET http://vlad153.sytes.net/api/users/
```

Регистрация пользователя

```
POST http://vlad153.sytes.net/api/users/
```

Профиль пользователя

```
GET http://vlad153.sytes.net/api/users/id/
```

Текущий пользователь
```
GET http://vlad153.sytes.net/api/users/me/
```

Изменение пароля
```
POST http://vlad153.sytes.net/api/users/set_password/
```

Получить токен авторизации
```
POST http://vlad153.sytes.net/api/auth/token/login/
```

Удаление токена
```
POST http://vlad153.sytes.net/api/auth/token/logout/
```

### Теги:

Cписок тегов

```
GET http://vlad153.sytes.net/api/tags
```

Получение тега

```
GET http://vlad153.sytes.net/api/tags/{id}/
```

### Рецепты:

Список рецептов

```
GET http://vlad153.sytes.net/api/recipes/
```

Создание рецепта

```
POST http://vlad153.sytes.net/api/recipes/
```

Получение рецепта

```
GET http://vlad153.sytes.net/api/recipes/id/
```

Обновление рецепта

```
PATCH http://vlad153.sytes.net/api/recipes/id/
```

Удаление рецепта
```
DELETE http://vlad153.sytes.net/api/v1/api/recipes/id/
```

### Список покупок:

Скачать список покупок

```
GET http://vlad153.sytes.net/api/recipes/download_shopping_cart/
```

Добавить рецепт в список покупок

```
PATCH http://vlad153.sytes.net/api/recipes/{id}/shopping_cart/
```

Удалить рецепт из списка покупок

```
DELETE http://vlad153.sytes.net/api/recipes/{id}/shopping_cart/


### Избранное:


Добавить рецепт в избранное

```
POST http://vlad153.sytes.net/api/recipes/{id}/favorite/
```

Удалить рецепт из избранного

```
DELETE http://vlad153.sytes.net/api/v1/auth/token/
```

### Подписки:

Мои подписки

```
GET http://vlad153.sytes.net/api/users/subscriptions/
```

Подписаться на пользователя

```
POST http://vlad153.sytes.net/api/users/{id}/subscribe/
```

Отписаться от пользователя

```
DELETE http://vlad153.sytes.net/api/users/{id}/subscribe/
```

### Ингредиенты:

Список ингредиентов

```
GET http://vlad153.sytes.net/api/ingredients/
```

Получение ингредиента

```
GET http://vlad153.sytes.net/api/users/subscriptions/
```