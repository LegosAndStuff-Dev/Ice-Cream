from random import random
import sqlite3
import random
from Disecon import *
from functions.database import *

def getCostWithLocation(userID: int):
    locationNum = getLocationNum(userID)

    locationNum += 1
    cost = 0
    payroll = locationNum * 850

    for i in range(locationNum):
        for ice in range(75):
            for i in range(3):
                whichIce = random.randint(1, 3)
                
                if whichIce == 1:
                    cost += 5

                elif whichIce == 2:
                    cost += 6

                elif whichIce == 3:
                    cost += 7

    cost = cost - payroll

    return cost
