# -*- coding: utf-8 -*-
"""
пример импорта из директории расположенной на уровень выше
"""
import sys

'''
import os
# 1-й вариант: добавление абсолютного пути
_path = os.path.split(os.path.abspath(__file__))[0]
_path = os.path.split(_path)[0]
if not _path in sys.path: 
    sys.path.append(_path)
'''
#  2-й вариант: добавление относительного пути
sys.path.append('../')

from moduleA import sss

def sss_run():
    sss()

