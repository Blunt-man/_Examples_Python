import threading
import time

locked_integer = 0
mylock = threading.Lock()

def thread_function(name, action_count):
    print("Thread",name,"starting")
    while action_count:
        time.sleep(2)
        print(name)
        shared_Action()
        action_count -=1
    print("Thread",name,"finishing")

def thread_another(name, action_count, delay):
    print("Thread",name,"starting")
    while action_count:
        time.sleep(delay)
        print(name)
        shared_Action()
        action_count -=1
    print("Thread",name,"finishing")

def shared_Action():
    global locked_integer
    mylock.acquire()
    locked_integer += 1
    print("locked",locked_integer,"times")
    mylock.release()

x = threading.Thread(target=thread_function, args=("Thread-1",15,))
y = threading.Thread(target=thread_another, args=("Thread-2", 15, 4, ))

x.start()
y.start()

x.join()
y.join()
print("Main Programm End")