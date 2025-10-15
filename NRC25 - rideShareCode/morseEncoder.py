import board
import digitalio
import time

led = digitalio.DigitalInOut(board.GP22)
led.direction = digitalio.Direction.OUTPUT
buz = digitalio.DigitalInOut(board.GP15)
buz.direction = digitalio.Direction.OUTPUT
sysled = digitalio.DigitalInOut(board.GP25)
sysled.direction = digitalio.Direction.OUTPUT

def go():
    led.value = True
    buz.value = True
    sysled.value = True

def stop():
    led.value = False
    buz.value = False
    sysled.value = False

def short():
    go()
    time.sleep(0.1)
    stop()
    time.sleep(0.5)

def long():
    go()
    time.sleep(0.5)
    stop()
    time.sleep(0.5)


def numbreak():
    time.sleep(1)

def cycbreak():
    time.sleep(2)
    go()
    time.sleep(5)
    stop()
    time.sleep(2)

def zero():
    long()
    long()
    long()
    long()
    long()
    numbreak()

def one():
    short()
    long()
    long()
    long()
    long()
    numbreak()

def two():
    short()
    short()
    long()
    long()
    long()
    numbreak()

def three():
    short()
    short()
    short()
    long()
    long()
    numbreak()

def four():
    short()
    short()
    short()
    short()
    long()
    numbreak()

def five():
    short()
    short()
    short()
    short()
    short()
    numbreak()

def six():
    long()
    short()
    short()
    short()
    short()
    numbreak()

def seven():
    long()
    long()
    short()
    short()
    short()
    numbreak()

def eight():
    long()
    long()
    long()
    short()
    short()
    numbreak()

def nine():
    long()
    long()
    long()
    long()
    short()
    numbreak()