#!/usr/bin/python3
import os, sys
sys.path.append("/usr/lib")
import _kipr as k

def stop():
    for i in range(4):
        k.motor(i, 0)

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

def main():
    speed = 35   
    threshold = 3800   

    while True: 
        left = k.analog(1)    # linker Tophat
        right = k.analog(0)   # rechter Tophat


        print("L:", left, "R:", right)  # Debug-Ausgabe

        if left > threshold and right > threshold:
            forward(speed)
        elif left <= threshold and right > threshold:
            turn_right(speed)    # Hier habe ich die Richtung umgetauscht
        elif right <= threshold and left > threshold:
            turn_left(speed)    # Hier hab ich left eingetragen statt left
        else:
            # Der Roboter fährt jetzt geradeaus wenn beide Sensoren
            # einen Wert für Weiß liefern.
            forward(speed);

main()
