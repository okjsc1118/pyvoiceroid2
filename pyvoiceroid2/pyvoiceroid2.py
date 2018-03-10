# -*- coding: utf-8 -*-

from config import *
import pyautogui
import pyperclip

class Voiceroid2Control:
    def __init__(self):
        self.__script = ''
        self.__script_area = ScriptArea()
        self.__play_button = PlayButton()
        self.__stop_button = StopButton()
        self.__head_button = HeadButton()
        self.__tail_button = TailButton()
            
    def get_script(self):
        return self.__script
        
    def set_text(self, text, talker=None):
        if talker:
            self.__script = talker + '> ' + text + '\r\n'
        else:
            self.__script = text + '\r\n'
            
    def append_text(self, text, talker=None):
        if talker:
            self.__script = self.__script + talker + '> ' + text + '\r\n'
        else:
            self.__script = self.__script + text + '\r\n'

    def reset_script(self):
        self.__script = ''
        
    def get_status(self):
        return ''

    def set_script(self):
        pyautogui.click(x=self.__script_area.x, y=self.__script_area.y)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('del')
        pyperclip.copy(self.__script)
        pyautogui.hotkey('ctrl', 'v')
        
    def play_voice(self):
        self.stop_voice()
        self.move_script_carsor()
        pyautogui.click(x=self.__play_button.x, y=self.__play_button.y)
        
    def stop_voice(self):
        pyautogui.click(x=self.__stop_button.x, y=self.__stop_button.y)
        
    def move_script_carsor(self, position='head'):
        if position == 'head':
            pyautogui.click(x=self.__head_button.x, y=self.__head_button.y)
        elif position == 'tail':
            pyautogui.click(x=self.__tail_button.x, y=self.__tail_button.y)
        else:
            print('move_script_carsor: Incorrect position.')