import time
import rtc
global f
global r

r = rtc.RTC()

def log(msg):
    f = open("Callisto.log", mode="a", encoding="utf-8")
    times = str(r.datetime.tm_year)+"/"+str(r.datetime.tm_mon)+"/"+str(r.datetime.tm_mday)+"	"+str(r.datetime.tm_hour)+":"+str(r.datetime.tm_min)+":"+str(r.datetime.tm_sec)
    mtime = str(time.monotonic())
    logm = times+"	"+mtime+"	"+str(msg)+"\n"
    f.write(logm)
    f.close()
    print(logm)
    
    
