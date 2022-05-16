import threading
import time

def thread_function(name):
    print("Thread",name,"starting")
    time.sleep(2)
    print("Thread",name,"finishing")

def thread_another(name, delay):
    print("Thread",name,"starting")
    time.sleep(delay)
    print("Thread",name,"finishing")

x = threading.Thread(target=thread_function, args=(1,))
y = threading.Thread(target=thread_another, args=("Thread-2", 4, ))
z = threading.Thread(target=thread_another, args=("Thread-3", 2, ))

x.start()
y.start()
z.start()

x.join()

print("Main Programm End")