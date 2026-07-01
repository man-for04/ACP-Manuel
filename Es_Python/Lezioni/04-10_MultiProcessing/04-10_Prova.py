import multiprocessing, os

from multiprocessing import Process

print(f'PID: {os.getpid()}, __name__:{__name__}')

def run_function(x):
    print(f'[run function] process ID: {os.getpid()}')
    print(f'valore di x: {x}')

if __name__ == "__main__":
    multiprocessing.set_start_method("fork")
    p1 = multiprocessing.Process(target=run_function, args=(20,))
    p1.start()
    p1.join()