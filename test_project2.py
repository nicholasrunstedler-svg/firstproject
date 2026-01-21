#from functions import cleanup_time
from multiprocessing import Pool, Process, Queue

def use_cpu(n: int):
    for i in range(1,n):
        calculate = i ** (1/i)
        #print(calculate)

if __name__ == "__main__":
    q = Queue()
    processes = []
    for i in range(4):
        p = Process(target=use_cpu, args=(i*10,))
        p.start()
        processes.append(p)

    for P in processes:
        P.join()
