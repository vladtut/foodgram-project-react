# проект foodgram-project-react

## URL проекта:

## Описание проекта:

Кулинарный онлайн-сервис и API для него. Пользователи могут создавать свои рецепты, читать рецепты других пользователей, подписываться на интересных авторов, добавлять лучшие рецепты в избранное, а также создавать список покупок, необходимых для приготовления выбранных блюд и скачивать его в PDF формате.


## Возможности сервиса:

+  делитесь своими рецептами
+  смотрите рецепты других пользователей
+  добавляйте рецепты в избранное
+  быстро формируйте список покупок, добавляя рецепт в корзину
+  следите за своими друзьями и коллегами


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
GET http://api.example.org/api/users/
```

Регистрация пользователя

```
POST http://api.example.org/api/users/
```

Профиль пользователя

```
GET http://api.example.org/api/users/id/
```

Текущий пользователь
```
GET http://api.example.org/api/users/me/
```

Изменение пароля
```
POST http://api.example.org/api/users/set_password/
```

Получить токен авторизации
```
POST http://api.example.org/api/auth/token/login/
```

Удаление токена
```
POST http://api.example.org/api/auth/token/logout/
```

### Теги:

Cписок тегов

```
GET http://api.example.org/api/tags
```

Получение тега

```
GET http://api.example.org/api/tags/{id}/
```

### Рецепты:

Список рецептов

```
GET http://api.example.org/api/recipes/
```

Создание рецепта

```
POST http://api.example.org/api/recipes/
```

Получение рецепта

```
GET http://api.example.org/api/recipes/id/
```

Обновление рецепта

```
PATCH http://api.example.org/api/recipes/id/
```

Удаление рецепта
```
DELETE http://api.example.org/api/v1/api/recipes/id/
```

### Список покупок:

Скачать список покупок

```
GET http://api.example.org/api/recipes/download_shopping_cart/
```

Добавить рецепт в список покупок

```
PATCH http://api.example.org/api/recipes/{id}/shopping_cart/
```

Удалить рецепт из списка покупок

```
DELETE http://api.example.org/api/recipes/{id}/shopping_cart/


### Избранное:


Добавить рецепт в избранное

```
POST http://api.example.org/api/recipes/{id}/favorite/
```

Удалить рецепт из избранного

```
DELETE http://api.example.org/api/v1/auth/token/
```

### Подписки:

Мои подписки

```
GET http://api.example.org/api/users/subscriptions/
```

Подписаться на пользователя

```
POST http://api.example.org/api/users/{id}/subscribe/
```

Отписаться от пользователя

```
DELETE http://api.example.org/api/users/{id}/subscribe/
```

### Ингредиенты:

Список ингредиентов

```
GET http://api.example.org/api/ingredients/
```

Получение ингредиента

```
GET http://api.example.org/api/users/subscriptions/
```