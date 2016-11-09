# Waseem Azher
# Program_2: dpa.py
# 8 November 2016
# The Dining Philosophers Problem: Four threads (the philosophers) must share
# resources (the spaghetti). To do so, they must acquire locks (the forks). 
# In so doing, they deny the other philosophers the opportunity to eat. One 
# approach to the problem is ResourceWarning hierarchy solution, wherein each
# philosopher is required to acquire the forks in a fixed order, which helps 
# prevent deadlock.

import threading
import os
from os import system
import curses
import locale
import time
import threading
import random
import json
import struct
from time import sleep


# Layout of the table (P = philosopher, f = fork):
#          P0
#       f3    f0
#     P3        P1
#       f2    f1
#          P2

# Number of philosophers at the table. 
# There'll be the same number of forks.
numPhilosophers = 4

# Lists to hold the philosophers and the forks.
# Philosophers are threads while forks are locks.
philosophers = []
forks = []

class Philosopher(threading.Thread):
    count = 0;
    def __init__(self, index,waiter):
        threading.Thread.__init__(self)
        self.index = index
        self.waiter=waiter

    def run(self):
        # Assign left and right fork
        leftForkIndex = self.index
        rightForkIndex = (self.index - 1) % numPhilosophers
        forkPair = ForkPair(leftForkIndex, rightForkIndex)

        # Eat forever
        while True:
           	with self.waiter:
			               # Initialze a count to keep track of how many times each philosopher 
						   # eaten in a row.
                           self.count +=1			
                           forkPair.pickUp()						   
                       	   print("Philosopher", self.index, "has eaten", self.count, "times in a row")
	                   time.sleep(0.1)
        	           forkPair.putDown()

class ForkPair:
    def __init__(self, leftForkIndex, rightForkIndex):
        # Order forks by index to prevent deadlock
        if leftForkIndex > rightForkIndex:
            leftForkIndex, rightForkIndex = rightForkIndex, leftForkIndex
        self.firstFork = forks[leftForkIndex]
        self.secondFork = forks[rightForkIndex]

    def pickUp(self):
        # Acquire by starting with the lower index
        self.firstFork.acquire()
        self.secondFork.acquire()

    def putDown(self):
        # The order does not matter here
        self.firstFork.release()
        self.secondFork.release()

if __name__ == "__main__":
    # Create philosophers and forks
    waiter = threading.Semaphore(1)
    for i in range(0, numPhilosophers):
        philosophers.append(Philosopher(i,waiter))
        forks.append(threading.Lock())

    # All philosophers start eating
    for philosopher in philosophers:
        philosopher.start()

    # Allow CTRL + C to exit the program
    try:
        while True: sleep(0.1)
    except (KeyboardInterrupt, SystemExit):
        os._exit(0)
