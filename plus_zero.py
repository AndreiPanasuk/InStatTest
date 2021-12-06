# -*- coding: utf-8 -*-
"""
2. Игра крестики-нолики.
  Модуль в котором
  - Класс для хранения состояния игрового поля
  - Алгоритм проверки состояния игрового поля (пусто, идет игра, 
  выигрыла одна из сторон)
  
"""

class PlusZero(object):
    
    def __init__(self, dimension=3):
        self._dim = dimension
        self._data = []
        for d in range(self._dim):
            arr = list(None for _ in range(self._dim))
            self._data.append(arr)
    
    def set(self, i, j, val):
        """Записать значение в ячейку
        
        Args:
            i (int): координата по горизонтали
            j (int): координата по вертикали
            val (bool): крестик (True), нолик (False)
        """
        self._data[i][j] = val
    
    def get(self, i, j):
        """Считать значение из ячейки
        
        Args:
            i (int): координата по горизонтали
            j (int): координата по вертикали
        
        Returns:
            (bool): крестик (True), нолик (False)
        """
        return self._data[i][j]
    
    def state(self):
        """Текущий статус
        
        Returns (str):
            'empty'    - пусто
            'run'      - идет игра
            'plus'     - выигрыш крестиков
            'zero'     - выигрыш ноликов
        """
        return self._state() or 'run'
    
    def _state(self):
        empty = True
        vplus = list(True for _ in range(self._dim))
        vzero = list(True for _ in range(self._dim))
        xplus = True
        yplus = True
        xzero = True
        yzero = True
        cnt = self._dim - 1
        for i in range(self._dim):
            plus = True
            zero = True
            for j in range(self._dim):
                val = self._data[i][j]
                if val is not None:
                    empty = False
                    if val:
                        zero = False
                        vzero[j] = False
                        if i==j:
                            xzero = False
                        elif i == cnt - j:
                            yzero = False                            
                    else:
                        plus = False
                        vplus[j] = False
                        if i==j:
                            xplus = False
                        elif i == cnt - j:
                            yplus = False                            
                else:
                    plus = False
                    zero = False
                    vplus[j] = False
                    vzero[j] = False
                    if i==j:
                        xzero = False
                        xplus = False
                    elif i == cnt - j:
                        yzero = False
                        yplus = False
            if plus:
                return 'plus'
            elif zero:
                return 'zero'
        if empty:
            return 'empty'
        elif xplus or yplus or tuple(x for x in vplus if x):
            return 'plus'
        elif xzero or yzero or tuple(x for x in vzero if x):
            return 'zero'
