# Примеры пользования различными библиотеками и фреймворками

## Kafka

Показан пример понятия одной ноды через компоуз файл, создание топиков
через баш-скрипт, поднятие веб-интерфейса, записи и чтения сообщения.

Запись и чтение можно запускать как локально, через `python main.py`, так и
через компоуз

Для запуска

- `cd kafka`
- `docker compose up -d`
- Опционально `python main.py`

Веб-интерфейс по адресу `localhost:8080`

## RabbitMQ

Показан пример поднятия RabbitMQ через docker compose и работы с ним через два
локальных python-файла.

Для запуска

- `cd rabbitmq`
- `docker compose up -d`
- `python -m pip install requirements.txt`
- `python send.py`
- `python receive.py`

## ClickHouse

Показан пример работы с кликхаус в режиме 2х2 (2 реплики, 2 шарда).
Показан пример записи и чтения на python в синхронном и асинхронном вариантах

Для запуска

- `cd clickhouse`
- `docker compose up -d`
- `python -m pip install requirements.txt`
- `python main.py`
- `python async.py`

## Spark

Показан пример запуска Spark через компоуз файл и работы с ним через Jupyter
notebook на основе датасета отзывов о мороженом.

Для запуска

- `cd spark`
- `docker compose up -d`
- `docker compose logs python`
- Перейти по ссылке из логов предыдущего шага (начинается
  на `127.0.0.1:8888/...`)
- В открывшемся окне перейти в директорию `workspace`
- Открыть и запустить `spark_test.ipynb` (`Kernel -> Restart & Run all`)

## MongoDB

Показан пример развертывания монго из компоуз файла и работы с монго через
синхронный pymongo
(запись и чтение)

Для запуска

- `cd mongo`
- `docker compose up -d`
- `python -m pip install requirements.txt`
- `python main.py`