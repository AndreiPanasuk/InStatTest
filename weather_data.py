# -*- coding: utf-8 -*-
"""
3. Используя модуль aiohttp и апи openweathermap.org реализовать 
получение данных по 3 городам в формате json. 
Полученные данные сохранить в файл
"""

import aiohttp
import asyncio

url = 'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={appid}'
 
async def weather(city, appid = '8451ad6c3fa0d7c026fa518c8820371e'):
    async with aiohttp.ClientSession() as session:
        _url = url.format(city = city, appid = appid)
        async with session.get(_url) as resp:
            fname = 'weathers/{}.json'.format(city)
            with open(fname, 'wb') as f:
                f.write(await resp.content.read())
                print('Weather data for "{0}" to file "{1}"'.format(city, fname))

async def _main(cities):
    tasks = tuple(weather(city) for city in cities)
    await asyncio.gather(*tasks)

def main(*cities):
    asyncio.run(_main(cities))
