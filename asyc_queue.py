import asyncio
import requests


async def queue_execution(arg_urls, callback, parallel=2):
    loop = asyncio.get_event_loop()
    queue = asyncio.Queue()

    for u in arg_urls:
        queue.put_nowait(u)

    async def fetch(q):
        while not q.empty():
            u = await q.get()
            future = loop.run_in_executor(None, requests.get, u)
            future.add_done_callback(callback)
            await future

    tasks = [fetch(queue) for ii in range(parallel)]
    return await asyncio.wait(tasks)

loop = asyncio.get_event_loop()
results = []


def store_result(f):
    results.append(f.result())

loop.run_until_complete(queue_execution([
    'http://example.com',
    'http://example.com',
    'http://example.com',
    ], store_result))
for res in results:
    print('queue execution: {}'.format(res))
