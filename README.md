# Инструкция по запуску Docker-Compose проекта

Следуйте этим шагам для запуска проекта:

## Шаг 1: Скачайте необходимые файлы

Скачайте следующие файлы в вашу локальную директорию:

- `docker-compose.yml`
- `init.sql`

## Шаг 2: Скачайте Docker-образ

Выполните следующую команду в терминале:

```bash
docker pull esternit/task7bd:latest
```

## Шаг 3: Проверьте свободные порты

Убедитесь, что порты **5432**, **5050** и **8000** свободны на вашем компьютере. Эти порты используются для доступа к базе данных, PgAdmin и вашему приложению соответственно.

## Шаг 4: Запустите проект

Запустите проект с помощью команды:

```bash
docker-compose up -d
```

## Шаг 5: Доступ к документации

После успешного запуска проекта, вы можете получить доступ к документации вашего приложения по следующей ссылке:
[http://localhost:8000/docs](http://localhost:8000/docs)

## Шаг 6: Код в репозитории

Исходный код проекта доступен в репозитории на GitHub:
[https://github.com/Esternit/Task7BD](https://github.com/Esternit/Task7BD) в папке `script/src/script.py`.

## Шаг 7: Данные для подключения к базе данных

Для подключения к базе данных (например, через PgAdmin на порту 5050) используйте следующие учетные данные:

- **POSTGRES_USER**: `user`
- **POSTGRES_PASSWORD**: `pass`
- **POSTGRES_DB**: `db`

## Шаг 8: Удаление Docker-образа

Если вы больше не планируете использовать проект, вы можете удалить Docker-образ с помощью команды:

```bash
docker rmi esternit/task7bd:latest
```
