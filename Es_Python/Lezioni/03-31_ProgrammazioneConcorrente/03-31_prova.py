from threading import Thread

class MyThread(Thread):

    def run(self):
        print("Running myThread...\n")
        print("is_alive?: ", self.is_alive())
    
    def method1(self):
        print("method1 invocato...\n")

m=MyThread(daemon=True)
m.start()
print("is_alive? esterno: ", m.is_alive())
m.join()
m.method1()
print("is_alive?: ", m.is_alive())