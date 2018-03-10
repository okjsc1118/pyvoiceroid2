# -*- coding: utf-8 -*-

"""
Set button position to control automatically.
Following params are examples.
"""

class Position:
    def __init__(self):
        self._x = 0
        self._y = 0
    
    @property
    def x(self):
        return self._x
        
    @property
    def y(self):
        return self._y
            
class ScriptArea(Position):
    def __init__(self):
        self._x = 500
        self._y = 300
        
class PlayButton(Position):
    def __init__(self):
        self._x = 330
        self._y = 660
        
class StopButton(Position):
    def __init__(self):
        self._x = 400
        self._y = 660

class HeadButton(Position):
    def __init__(self):
        self._x = 470
        self._y = 660

class TailButton(Position):
    def __init__(self):
        self._x = 540
        self._y = 660