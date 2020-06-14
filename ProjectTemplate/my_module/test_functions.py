"""Test for my functions"""

import pygame
import time
import random
import pytest

from my_module.classes import StartGame
from my_module.functions import run_timer

def test_run_timer():
    assert run_timer() == print("You have finished collecting the blocks!")
    
test_run_timer()

def test_StartGame_1():
    
    testing = StartGame()
    testing.__init__()
    
    assert testing.black == (0, 0, 0)
    assert testing.white == (255, 255, 255)
    assert testing.periwinkle == (100, 0, 255)
    
    assert testing.x1_change == 0
    assert testing.y1_change == 0
    
test_StartGame_1()

    



                 
    