#!/usr/bin/python3
import os, sys
sys.path.append("/usr/lib")
import _kipr as k

def stop(speed):
    for i in range(4):
        k.motor(i, speed)

def forward(speed):
    k.motor(0, -speed)
    k.motor(1, -speed)
    k.motor(2, speed)
    k.motor(3, speed)

def turn_left(speed):
    k.motor(0, -speed)
    k.motor(1, -speed)
    k.motor(2, -speed)
    k.motor(3, -speed)

def turn_right(speed):
    k.motor(0, speed)
    k.motor(1, speed)
    k.motor(2, speed)
    k.motor(3, speed)

def backward(speed):
    k.motor(0, speed)
    k.motor(1, speed)
    k.motor(2, -speed)
    k.motor(3, -speed)

def main():
    speed = 35   
    threshold = 3800   # white<3800 | black>=3800  

    while True: 
        left = k.analog(1)    # linker Tophat
        right = k.analog(0)   # rechter Tophat
        
        print("L:", left, "R:", right)  # Values

        if left > threshold and right > threshold:
            for i in range(0, 40, 1):
                forward(i)
        elif left < threshold and right >= threshold:
            for i in range(40, 20, -1):    
                stop(i)
            for i in range(0, 40, 1):    
                turn_right(i)  
        elif right < threshold and left >= threshold:
            for i in range(40, 20, -1):
                stop(i)    
            for i in range(0, 40, 1):                
                turn_left(i)
        elif left < threshold and right < threshold:
            for i in range(40, 0, -1):    
                stop(i)
            backward(speed)
            
    
main()
