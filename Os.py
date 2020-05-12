import threading
import urllib.request
import os
import multiprocessing

print("Number of core is >",multiprocessing.cpu_count())
nCore = multiprocessing.cpu_count()
#load1,load5,load15 = os.getloadavg()
#print("Load average for 5 minutes", load5)
#if  nCore-load5 <1:
#    print("Exit")
#   exit()

def urlCheck(url):
    req = urllib.request.urlopen(url)
    print(req)

thread1 = threading.current_thread()
t1 = threading.Thread(target=urlCheck, args=("https://api.github.com",))
t2 = threading.Thread(target=urlCheck, args=("http://bilgisayar.mu.edu.tr/",))
t3 = threading.Thread(target=urlCheck, args=("https://www.python.org/",))
t4 = threading.Thread(target=urlCheck, args=("http://akrepnalan.com/ceng2034",))
t5 = threading.Thread(target=urlCheck, args=("https://api.github.com",))
t6 = threading.Thread(target=urlCheck, args=("https://github.com/caesarsalad/wow",))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
