import asyncio
import json

import aio_pika


async def main():
    connection = await aio_pika.connect_robust("amqp://guest:guest@localhost/")
    async with connection:
        channel = await connection.channel()

        exchange = await channel.declare_exchange("users", aio_pika.ExchangeType.DIRECT)
        queue = await channel.declare_queue("clicks", durable=True)

        await queue.bind(exchange, "clicks")

        message = aio_pika.Message(
            body=json.dumps(
                {"user_id": 1, "clicked_element": "button1", "click_time": "10:30:00"}
            ).encode(),
            delivery_mode=aio_pika.DeliveryMode.PERSISTENT,
        )

        await exchange.publish(message, routing_key="clicks")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
