import pandas as pd
import time
from matplotlib import pyplot as plt
from scipy.integrate import simpson
from numpy import trapz
import numpy
from scipy.interpolate import make_interp_spline, BSpline
plt.rcParams["figure.figsize"] = [10.00, 5.00]
plt.rcParams["figure.autolayout"] = True
plt.rcParams["figure.dpi"] = 600
print("Importing Data")
columns = ["Iter","MT","Alt","Temp","Humid","Press","aX","aY","aZ","SysTemp"]
df = pd.read_csv("CSV.csv", usecols=columns)

iter = list(df.Iter)
mt = list(df.MT)
mt2 = list(df.MT)
alt = list(df.Alt)
temp = list(df.Temp)
humid = list(df.Humid)
press = list(df.Press)
ax = list(df.aX)
ay = list(df.aY)
az = list(df.aZ)
sys = list(df.SysTemp)

for i in range(0,len(ax)):
    ax[i] = ax[i] * 9.81
    
for i in range(0,len(ay)):
    ay[i] = ay[i] * 9.81
    
for i in range(0,len(az)):
    az[i] = az[i] * 9.81

print("Plotting Data")

xx = []
for i in mt:
    xx.append(2500)

xnew = numpy.linspace(min(mt), max(mt), 3000)
plt.xlabel("Time From MCU Power On (s)")

### Altitude ###
plt.title("Callisto | Altitude Plot")
plt.plot(mt, alt,label='Altitude')
plt.ylabel("Altitude (ft)")
txt = "Apogee: "+str(max(alt))
plt.figtext(.7, .3, txt)
axis1 = plt.gca()
axis1.set_ylim([0, 2600])
plt.plot(mt,xx)
plt.savefig("alt.png")
plt.clf()

### Temperature ###
plt.title("Callisto | Temperature Plot")
plt.plot(mt, temp,label='Temperature')
plt.ylabel("Temperature (C)")
txt = "Minimum: "+str(min(temp))
plt.figtext(.7, .3, txt)
plt.savefig("temp.png")
plt.clf()

### Pressure ###
plt.title("Callisto | Pressure Plot")
spla = make_interp_spline(mt, press, k=3)
plt.plot(mt, press,label='Pressure')
plt.ylabel("Pressure (mBar)")
txt = "Minimum: "+str(min(press))
plt.figtext(.7, .3, txt)
plt.savefig("press.png")
plt.clf()

### Humidity ###
plt.title("Callisto | Humidity Plot")
spla = make_interp_spline(mt, humid, k=3)
plt.plot(mt, humid,label='Humidity')
plt.ylabel("Relative Humidity (%)")
plt.savefig("humid.png")
plt.clf()

### SysTemp ###
plt.title("Callisto | SystemTemperature Plot")
plt.plot(mt, sys,label='SysTemp')
plt.ylabel("System Temperature (C)")
plt.savefig("systemp.png")
plt.clf()

### Accelerometer ###
plt.title("Callisto | Accelerometer Plot")
plt.plot(mt, ax,label='X')
plt.plot(mt, ay,label='Y')
plt.plot(mt, az,label='Z')
plt.ylabel("Acceleration (m/s^2)")
txt = "Maximum: "+str(max([max(ax),max(ay),max(az)]))
plt.legend()
plt.figtext(.7, .3, txt)
plt.savefig("acc.png")
plt.clf()


### Velocity ###
g = 9.81
x1,x2,x3 = [0],[0],[0]
for i in range(0,len(ax)-1):
    dt = mt[i+1] - mt[i]
    x1.append(x1[i] + dt*ax[i])
for i in range(0,len(ay)-1):
    dt = mt[i+1] - mt[i]
    x2.append(x2[i] + dt*ay[i])
for i in range(0,len(az)-1):
    dt = mt[i+1] - mt[i]
    x3.append(x3[i] + dt*az[i])
plt.title("Callisto | Velocity Plot")
plt.plot(mt, x1,label='X')
plt.plot(mt, x2,label='Y')
plt.plot(mt, x3,label='Z')
plt.ylabel("Velocity (m/s)")
txt = "Maximum: "+str(max([max(x1),max(x2),max(x3)]))
plt.legend()
plt.figtext(.7, .3, txt)
plt.savefig("velo.png")
plt.clf()

### Vert Speed ###
mt.pop(len(mt)-1)
plt.title("Callisto | Vertical Speed Plot")
vs = []
try:
    for i in range(0,len(mt2)):
        dh = (alt[i+1]-alt[i])/3.281
        dt = mt2[i+1]-mt2[i]
        vs.append(dh/dt)
except IndexError:
    pass
plt.plot(mt, vs,label='Vertical Speed')
plt.ylabel("Vertical Speed (m/s)")
txt = "Maximum: "+str(max(vs))
plt.figtext(.7, .3, txt)
plt.savefig("vs.png")
plt.clf()



input("\n\n\nEND OF SCRIPT")