from multiprocessing import Pool, Process
import time
import os
#os.system('cls')

def square(x):
    print(x**2, end='\n')
    return x**2

def print_something() -> None:
    print("Hello World")
    time.sleep(.5)

#if __name__ == '__main__':
#    processes = []
#    p = Process(target=print_something)
#    p.start()
#
#    p.join()

if __name__ == "__main__":
    processes = []
    for i in range(5):
        p = Process(target=square, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

