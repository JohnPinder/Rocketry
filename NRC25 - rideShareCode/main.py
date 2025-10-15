import csvDriver as csv
import LIS3DHdriver as acc
from bme280 import basic as bmem
import morseEncoder as me
import board
import busio
import lis3dh as lis3dhm
import time

global status
global altlog
global test

csv.init()
test = True
status = 0
altlog = []
td = 0.5


# Altitude to trigger apogee detection
reclim = 5

i2c = busio.I2C(board.GP21, board.GP20)
bme = bmem.Adafruit_BME280_I2C(i2c)
l3d = lis3dhm.LIS3DH_I2C(i2c, address=0x19)

bme.overscan_pressure = 0x02

l3d.range = lis3dhm.RANGE_2_G

bme.sea_level_pressure = bme.pressure

def appoproc(alt):
   ls = [int(d) for d in str(alt)]
   print(ls)
   for i in ls:
       if i == 0:
           me.zero()
       elif i == 1:
           me.one()
       elif i == 2:
           me.two()
       elif i == 3:
           me.three()
       elif i == 4:
           me.four()
       elif i == 5:
           me.five()
       elif i == 6:
           me.six()
       elif i == 7:
           me.seven()
       elif i == 8:
           me.eight()
       elif i == 9:
           me.nine()
   me.cycbreak()


# def appoproc(alt):
    # print(str(alt))

def log(alt):
    global altlog
    altlog.append(round(alt,0))

def apogee():
    global altlog
    app = max(altlog)
    altlog = []
    while True:
        appoproc(app)
        temp = bme.temperature
        humid = bme.relative_humidity
        press = bme.pressure
        ax, ay, az = [value / lis3dhm.STANDARD_GRAVITY for value in l3d.acceleration]
        alt = bme.altitude
        if test == True:
            csv.test(alt,temp,humid,press,ax,ay,az)
        else:
            csv.write(alt,temp,humid,press,ax,ay,az)

while True:
    time.sleep(td)
    temp = bme.temperature
    humid = bme.relative_humidity
    press = bme.pressure
    ax, ay, az = [value / lis3dhm.STANDARD_GRAVITY for value in l3d.acceleration]
    alt = int(bme.altitude)
    if alt < reclim:
        if status == 1:
            apogee()
        else:
            pass
    else:
        if status == 0:
            status = 1
            td = 0
            log(alt)
        else:
            log(alt)

    if test == True:
        csv.test(alt,temp,humid,press,ax,ay,az)
    else:
        csv.write(alt,temp,humid,press,ax,ay,az)