# -*- coding: utf-8 -*-

print(
"""
1. Написать пример используя импорт из директории расположенной на 
    уровень выше.
    реализовано в файле project.prg1, работа импорта: 
"""
)
from project.prg1 import sss_run 
sss_run()

print(
"""
2. Игра крестики-нолики.
  Модуль в котором
  - Класс для хранения состояния игрового поля
  - Алгоритм проверки состояния игрового поля (пусто, идет игра, 
  выигрыла одна из сторон)
  
"""
)
from plus_zero import PlusZero

pz = PlusZero()
print(pz.state())
val = False
pz.set(0,0,val)
print(pz.state())
pz.set(1,1,val)
pz.set(2,2,val)
print(pz.state())

print(
"""
3. Используя модуль aiohttp и апи openweathermap.org реализовать 
    получение данных по 3 городам в формате json. 
    Полученные данные сохранить в файл
"""
)
from weather_data import main
main('Moscow', 'London', 'Paris')