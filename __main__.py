import time

from balloon import Balloon
from clown import Clown

def current_time_ms():
    return round (time.time() * 1000)

clown = Clown()
print(current_time_ms())
first_balloon = clown.buy_balloon(3)
second_balloon = Balloon("Blue")
balloon_list = []
for i in range(10):
    balloon_list.append(Balloon("Green"))

first_balloon().update(current_time_ms())
first_balloon.pop()

for balloon in balloon_list:
    print(balloon)
    print(f"Other way: {balloon.color}: {balloon.volume_ml}")
