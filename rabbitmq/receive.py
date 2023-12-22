import asyncio
import json

import aio_pika


async def on_message(message: aio_pika.IncomingMessage):
    async with message.process():
        msg_body = message.body.decode()
        msg_dict = json.loads(msg_body)
        print("Received message", msg_dict)


async def main():
    connection = await aio_pika.connect_robust("amqp://guest:guest@localhost/")
    async with connection:
        channel = await connection.channel()

        queue = await channel.declare_queue("clicks", durable=True)

        await queue.consume(callback=on_message)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
