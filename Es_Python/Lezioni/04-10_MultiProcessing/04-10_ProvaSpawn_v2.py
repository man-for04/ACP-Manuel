import multiprocessing, os

from multiprocessing import Process

print(f'PID: {os.getpid()}, __name__:{__name__}')

def run_function(x):
    print(f'[run function] process ID: {os.getpid()}')
    print(f'valore di x: {x}')

if __name__ == "__main__": #tutto quello che abbiamo qui potremmo pensare che venga copiato nel figlio, ma ciò nella spawn NON AVVIENE. Se è definito in padre ma non esplicitamente serializzato in figlio, non potrei usarlo
    p1 = multiprocessing.Process(target=run_function, args=(20,))
    p1.start()
    p1.join()
