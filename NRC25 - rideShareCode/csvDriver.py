import circuitpython_csv as csv
import rtc
import time
import microcontroller as mcu

def init():
    global systemsen
    global iter
    global r
    f = open("CSV.csv", mode="a", encoding="utf-8")
    csvf = csv.writer(f)
    csvf.writerow(["Iter","MT","Time","Alt","Temp","Humid","Press","aX","aY","aZ","SysTemp"])
    f.close()
    r = rtc.RTC()
    iter = 0
    #rtc.set_time_source(time.struct_time((2025,5,4,10,48,30,0,0,0)))

def write(alt,temp,humid,press,ax,ay,az):
    global iter
    iter = iter + 1
    times = str(r.datetime.tm_hour)+str(r.datetime.tm_min)+str(r.datetime.tm_sec)
    mtime = time.monotonic()
    systemp = round(mcu.cpu.temperature,1)
    with open("CSV.csv", mode="a", encoding="utf-8") as f:
        csvf = csv.writer(f)
        csvf.writerow([str(iter),str(mtime),times,str(alt),str(temp),str(humid),str(press),str(ax),str(ay),str(az),str(systemp)])
        
def test(alt,temp,humid,press,ax,ay,az):
    global iter
    iter = iter + 1
    times = str(r.datetime.tm_hour)+str(r.datetime.tm_min)+str(r.datetime.tm_sec)
    mtime = time.monotonic()
    systemp = round(mcu.cpu.temperature,1)
    print([str(iter),str(mtime),times,str(alt),str(temp),str(humid),str(press),str(ax),str(ay),str(az),str(systemp)])
