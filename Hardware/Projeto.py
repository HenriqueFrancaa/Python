import RPi.GPIO as gpio
import time

led1 = 17
led2 = 27
led3 = 22
led4 = 9
led5 = 10
led6 = 11
led7 = 13
led8 = 19
led9 = 26
 
gpio.setmode(gpio.BCM)
gpio.setup(led1,gpio.OUT)
gpio.setup(led2,gpio.OUT)
gpio.setup(led3,gpio.OUT)
gpio.setup(led4,gpio.OUT)
gpio.setup(led5,gpio.OUT)
gpio.setup(led6,gpio.OUT)
gpio.setup(led7,gpio.OUT)
gpio.setup(led8,gpio.OUT)
gpio.setup(led9,gpio.OUT)

def sequencia3():
    gpio.output(led3,gpio.HIGH)
    time.sleep(1)
    gpio.output(led3,gpio.LOW)
    time.sleep(1)
    gpio.output(led2,gpio.HIGH)
    gpio.output(led6,gpio.HIGH)
    time.sleep(1)
    gpio.output(led2,gpio.LOW)
    gpio.output(led6,gpio.LOW)
    time.sleep(1)
    gpio.output(led1,gpio.HIGH)
    gpio.output(led5,gpio.HIGH)
    gpio.output(led9,gpio.HIGH)
    time.sleep(1)
    gpio.output(led1,gpio.LOW)
    gpio.output(led5,gpio.LOW)
    gpio.output(led9,gpio.LOW)
    time.sleep(1)
    gpio.output(led4,gpio.HIGH)
    gpio.output(led8,gpio.HIGH)
    time.sleep(1)
    gpio.output(led4,gpio.LOW)
    gpio.output(led8,gpio.LOW)
    time.sleep(1)
    gpio.output(led7,gpio.HIGH)
    time.sleep(1)
    gpio.output(led7,gpio.LOW)

def sequencia7():
    gpio.output(led7,gpio.HIGH)
    time.sleep(1)
    gpio.output(led4,gpio.HIGH)
    gpio.output(led8,gpio.HIGH)
    time.sleep(1)
    gpio.output(led1,gpio.HIGH)
    gpio.output(led5,gpio.HIGH)
    gpio.output(led9,gpio.HIGH)
    time.sleep(1)
    gpio.output(led2,gpio.HIGH)
    gpio.output(led6,gpio.HIGH)
    time.sleep(1)
    gpio.output(led3,gpio.HIGH)
    time.sleep(1)
    gpio.output(led7,gpio.HIGH)
    gpio.output(led4,gpio.HIGH)
    gpio.output(led8,gpio.HIGH)
    gpio.output(led9,gpio.HIGH)
    gpio.output(led5,gpio.HIGH)
    gpio.output(led1,gpio.HIGH)
    gpio.output(led6,gpio.HIGH)
    gpio.output(led2,gpio.HIGH)

def sequencia11():
    gpio.output(led3,gpio.HIGH)
    time.sleep(1)
    gpio.output(led2,gpio.HIGH)
    gpio.output(led6,gpio.HIGH)
    time.sleep(1)
    gpio.output(led1,gpio.HIGH)
    gpio.output(led5,gpio.HIGH)
    gpio.output(led9,gpio.HIGH)
    time.sleep(1)
    gpio.output(led4,gpio.HIGH)
    gpio.output(led8,gpio.HIGH)
    time.sleep(1)
    gpio.output(led7,gpio.HIGH)
    time.sleep(1)
    gpio.output(led3,gpio.LOW)
    gpio.output(led2,gpio.LOW)
    gpio.output(led6,gpio.LOW)
    gpio.output(led9,gpio.LOW)
    gpio.output(led5,gpio.LOW)
    gpio.output(led1,gpio.LOW)
    gpio.output(led8,gpio.LOW)
    gpio.output(led4,gpio.LOW)
    gpio.output(led7,gpio.LOW)






