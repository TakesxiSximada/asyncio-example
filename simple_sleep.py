#! /usr/bin/env python
import asyncio

NAME_SECONDS = [
    ('first', 5),
    ('second', 0),
    ('third', 3),
    ]


async def sleeping(order, seconds, hook=None):
    await asyncio.sleep(seconds)
    if hook:
        hook(order)
    return order

async def basic_async(num):
    for s in NAME_SECONDS:
        res = await sleeping(*s)
        print('{}: {} is finished'.format(num, res))
    return True

loop = asyncio.get_event_loop()
for ii in range(10):
    asyncio.ensure_future(basic_async(ii))
loop.run_forever()
