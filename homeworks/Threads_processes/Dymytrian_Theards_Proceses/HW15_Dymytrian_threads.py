
import time
import threading

def print_text():
    print("This is method, that outputs the given text:")

    print("and considers number of active threads:", threading.active_count())
    time.sleep(2)

thread1 = threading.Thread(target=print_text)
thread2 = threading.Thread(target=print_text)
thread3 = threading.Thread(target=print_text)

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()