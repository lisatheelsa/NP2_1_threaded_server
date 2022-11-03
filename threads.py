import threading
from time import sleep

total = 100
t_lock = threading.Lock()

def proc(n):
    global total
    t_lock.acquire()
    if total >= n:
      total -= n
    t_lock.release()
    print("New thread", n,  total)

t = [threading.Thread(target = proc, args = [30]) for i in range(10)]

[ti.start() for ti in t]
[ti.join() for ti in t]

print("Main thread", total)