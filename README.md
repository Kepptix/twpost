# Start

В директории бота пишите

```
pip install poetry
poetry install
```

В файле .env вносите

- BOT_TOKEN - токен бота в <code>@botfather</code>
- APP_ID - id расширения твича
- APP_SECRET - секретный код расширения

После чего пишите эту команду

```
poetry run python -m src
```

# Settings

Для изменения пользователя у которого будет парситься тайтл стрима используйте команду

```
/change_user
```

Для изменения канала в который будет отправлятся уведомление используйте команду

```
/change_channel
```

Посмотреть id канала можно либо с помощью настройки в телеграме

- Settings
- Advanced
- Experimental settings
- Show Peer IDs in Profile

После чего в профиле чата/канала/пользователя будет его id 

Либо в боте <code>@myidbot</code>

Туда пересылаете сообщение с канала и он выдает его id
