# working out the kinks in asynchronous programming

import asyncio as aio
import time

import requests_async as requests

async def async_sleep(t):
    await aio.sleep(t)

async def compute_s():
    await async_sleep(2)
    print('done with s.')

async def compute_m():
    await async_sleep(4)
    print('done with m.')

async def compute_l():
    await async_sleep(1)
    print('done with l.')

async def main():
    t = time.perf_counter()
    await aio.gather(
        compute_s(),
        compute_m(),
        compute_l()
    )
    print(f'done in {time.perf_counter() - t:.4f}s.')

aio.run(main())