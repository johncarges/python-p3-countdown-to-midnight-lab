# your code goes here!
import time

def countdown(start):
    while start > 0:
        print(f"{start} SECOND(S)!")
        start -=1
    print("HAPPY NEW YEAR!")
    pass

def countdown_with_sleep(start):
    while start > 0:
        print(f"{start} SECOND(S)!")
        start -=1
        time.sleep(1)
    print("HAPPY NEW YEAR!")
    pass
