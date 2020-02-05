import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f"started at {time.strftime('%X')}")
    # 顺序执行没有并发
    # await say_after(1, "hello")
    # await say_after(2, "world")

    task_hello = asyncio.create_task(say_after(1, "Hello"))
    task_world = asyncio.create_task(say_after(2, "World"))
    await task_hello
    await task_world

    print(f"finished at {time.strftime('%X')}")


if __name__ == '__main__':
    asyncio.run(main())
