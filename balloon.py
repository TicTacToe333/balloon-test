import time

from thing import Balloon

def current_time_ms():
    return round (time.time() * 1000)

print(current_time_ms())
first_balloon = Balloon()
second_balloon = Balloon()
balloon_list = []
for i in range(10):
    balloon_list.append(Balloon("Green"))

first_balloon().update(current_time_ms())
first_balloon.pop()

for balloon in balloon_list:
    print(balloon)
    print(f"Other way: {balloon.color}: {balloon.volume_ml}")
