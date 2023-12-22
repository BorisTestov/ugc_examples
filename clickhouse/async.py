import asyncio

from aiochclient import ChClient
from aiohttp import ClientSession


async def main():
    async with ClientSession() as s:
        client = ChClient(s)
        assert await client.is_alive()  # возвращает True, если соединение успешно

        result = await client.execute(
            "CREATE DATABASE IF NOT EXISTS example ON CLUSTER company_cluster"
        )
        result = await client.execute(
            "CREATE TABLE IF NOT EXISTS example.regular_table "
            "ON CLUSTER company_cluster ("
            "id Int64, "
            "x Int32"
            ") Engine=MergeTree() ORDER BY id"
        )
        await client.execute(
            "INSERT INTO example.regular_table (id, x) VALUES", (1, 10), (2, 20)
        )
        result = await client.fetch("SELECT * FROM example.regular_table")
        for record in result:
            print(dict(record))


if __name__ == "__main__":
    asyncio.run(main())
