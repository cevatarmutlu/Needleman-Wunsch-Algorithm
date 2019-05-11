import threading


class MyThread(threading.Thread):
    def __init__(self, func_name):
        threading.Thread.__init__(self)
        self.func_name = func_name

    def run(self):
        self.func_name()


