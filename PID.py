import os 
from threading import Thread


def fun1():

    # Get the process ID of 
    # the current process 
    pid = os.getpid() 
    print ("hilo hijo: ", pid)


# Print the process ID of 
# the current process 
 
if __name__ == "__main__":
    pid = os.getpid() 
    print (pid)
    print("Soy el proceso padre")
    thread = Thread(target=fun1)
    thread.start()
    thread.join()
