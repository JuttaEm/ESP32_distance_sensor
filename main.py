import distance
import machine
import time


#tim1 = machine.Timer(1)

count = 0


def increase_counter(tim1):
    global count
    count += 1
    return count


# tim1.init(period=3000, mode=machine.Timer.PERIODIC,
    # callback=lambda t: increase_counter)

try:
    while True:
        dist = distance.get_distance()
        if dist < 50:
            print(dist)
            count += 1
            print(count)
        time.sleep(4)
except KeyboardInterrupt:
    pass
