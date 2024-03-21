# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 10:32:56 2024

@author: Administrator
"""

import random

def dice_roll():
    number = random.randint(1,6)
    return number

print("This is a 6-eyed-die roller")
number = dice_roll()
print("Your die is ", number)
