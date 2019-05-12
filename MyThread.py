import threading


class MyThread(threading.Thread):
    def __init__(self, func_name, first, last):
        threading.Thread.__init__(self)
        self.func_name = func_name
        self.first = first
        self.last = last

    def run(self):
        self.func_name(self.first, self.last)


