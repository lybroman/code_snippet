"""
### This script requires python3 env for asyncio lib
### Targeting for I/O Bound
"""
import timeit, requests

urls = {'https://httpstat.us/200?sleep=1000', 'https://httpstat.us/200?sleep=3000', 'https://httpstat.us/200?sleep=2000',
        'https://httpstat.us/200?sleep=2500', 'https://httpstat.us/200?sleep=500', 'https://httpstat.us/200?sleep=1500'}


def test_thread():
    import threading, queue
    q = queue.Queue()

    def worker():
        url = q.get()
        requests.get(url)
        q.task_done()

    num = len(urls)
    for i in range(num):
        q.put(urls[i])

    for i in range(num):
        th = threading.Thread(target=worker)
        th.start()

    q.join()


def test_process():
    from multiprocessing import Process, JoinableQueue
    q = JoinableQueue()

    def worker():
        url = q.get()
        requests.get(url)
        q.task_done()

    num = len(urls)
    for i in range(num):
        q.put(urls[i])

    for i in range(num):
        th = Process(target=worker)
        th.start()

    q.join()


def test_asyncio():
    import asyncio, aiohttp

    async def worker(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                await resp.text()

    coros = [worker(url) for url in urls]
    asyncio.set_event_loop(asyncio.new_event_loop())
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(asyncio.wait(coros))
    event_loop.close()


def test_asyncio_uvloop():
    import asyncio, aiohttp, uvloop

    async def worker(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                await resp.text()

    coros = [worker(url) for url in urls]
    asyncio.set_event_loop(uvloop.new_event_loop())
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(asyncio.wait(coros))
    event_loop.close()


print(timeit.timeit('test_thread()        ', setup="from __main__ import test_thread        ", number=10) / 10)
print(timeit.timeit('test_process()       ', setup="from __main__ import test_process       ", number=10) / 10)
print(timeit.timeit('test_asyncio()       ', setup="from __main__ import test_asyncio       ", number=10) / 10)
print(timeit.timeit('test_asyncio_uvloop()', setup="from __main__ import test_asyncio_uvloop", number=10) / 10)

