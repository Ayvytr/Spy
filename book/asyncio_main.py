import asyncio
import threading
import time


async def hello():
    print('Hello World:{} {}'.format(time.time(), threading.currentThread()))
    await asyncio.sleep(1)
    print('Hello Again:{} {}'.format(time.time(), threading.currentThread()))

# def run():
#     for i in range(5):
#         loop.run_until_complete(hello())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [hello(), hello()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
