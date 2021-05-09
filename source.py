import time
import threading


def main():
    print("This is a python clock with seconds")
    print("Type Y if you would like to start | anything else to close")
    yw = input()

    if yw == 'y' or yw == 'Y':
        printit()
    else:
        exit()

def printit():
    threading.Timer(1.0, printit).start()
    t = time.localtime()
    current_time = time.strftime("%I:%M:%S", t)
    print(current_time)


main()
