import os, sys
import detection3
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

def search():
    direction = detection3.get_direction()
    while direction == "N":
        turn_left(10)

def main():
    speed = 35

    while True:
        direction = detection3.get_direction()
        if direction == "R":
            turn_right(10)
        elif direction == "L":
            turn_left(10)
        elif direction == "Z":
            forward(10)
        elif direction == "N":
            search()

main()