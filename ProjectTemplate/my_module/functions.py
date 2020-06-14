"""A collection of function for doing my project."""

import random
import time

def run_timer():
    
    """ Creates a timer that initializes automatically when run and is quit when the user presses enter
    
    Returns
    ----------
    print statements listed below """
    
    start_time = time.time()
    print(start_time)
    stopper = input("Press enter to stop")
    end_time = time.time()
    print("You have finished collecting the blocks!")
    duration = int(end_time - start_time)
    if duration > 25:
        print("You were too slow collecting the blocks, better luck next time")
    else: 
        print("Good job speedy, you collected all the blocks before time ran out!")
