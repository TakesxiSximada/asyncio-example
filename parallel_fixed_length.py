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


async def parallel_by_gather():
    def notify(order):
        print(order + ' has just finished.')

    cors = [
        sleeping(name, seconds, hook=notify)
        for name, seconds in NAME_SECONDS]

    results = await asyncio.gather(*cors)
    return results


loop = asyncio.get_event_loop()
results = loop.run_until_complete(parallel_by_gather())
for res in results:
    print('asyncio.gather result: {}'.format(res))
