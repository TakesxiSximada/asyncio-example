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


async def parallel_by_await():
    def notify(order):
        print(order + ' has just finished.')

    cors = [
        sleeping(name, seconds, hook=notify)
        for name, seconds in NAME_SECONDS]
    done, pending = await asyncio.wait(cors)
    return done, pending


loop = asyncio.get_event_loop()
done, pending = loop.run_until_complete(parallel_by_await())
for d in done:
    dr = d.result()
    print('asyncio.wait result: {}'.format(dr))
