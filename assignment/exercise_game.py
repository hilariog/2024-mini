"""
Response time - single-threaded
"""

from machine import Pin
import random
import json
import time
import network
import ufirestore

def connect_to_internet(ssid, password):
    # Pass in string arguments for ssid and password
    
    # Just making our internet connection
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    # Wait for connect or fail
    max_wait = 10
    while max_wait > 0:
      if wlan.status() < 0 or wlan.status() >= 3:
        break
      max_wait -= 1
      print('waiting for connection...')
      time.sleep(1)
    # Handle connection error
    if wlan.status() != 3:
       raise RuntimeError(wlan.status())
    else:
      print('connected')
      status = wlan.ifconfig()
      
connect_to_internet('BU Guest (unencrypted)', '')

ufirestore.set_project_id("miniproject-efe95")
ufirestore.set_access_token("https://oauth2.googleapis.com/token")

document_path = "ResponseData"

N: int = 10
sample_ms = 10.0
on_ms = 500


def random_time_interval(tmin: float, tmax: float) -> float:
    """return a random time interval between max and min"""
    return random.uniform(tmin, tmax)


def blinker(N: int, led: Pin) -> None:
    # %% let user know game started / is over

    for _ in range(N):
        led.high()
        time.sleep(0.1)
        led.low()
        time.sleep(0.1)


def write_json(json_filename: str, data: dict) -> None:
    """Writes data to a JSON file.

    Parameters
    ----------

    json_filename: str
        The name of the file to write to. This will overwrite any existing file.

    data: dict
        Dictionary data to write to the file.
    """

    with open(json_filename, "w") as f:
        json.dump(data, f)


def scorer(t: list[int | None]) -> None:
    # %% collate results
    misses = t.count(None)
    print(f"You missed the light {misses} / {len(t)} times")

    t_good = [x for x in t if x is not None]

    print(t_good)

    # add key, value to this dict to store the minimum, maximum, average response time
    # and score (non-misses / total flashes) i.e. the score a floating point number
    # is in range [0..1]
    if misses<=9:
        average_response = sum(t_good) / len(t_good)
        min_value = min(t_good)
        max_value = max(t_good)
        score = sum(t_good) / N
    else:
        average_response=0
        min_value = 0
        max_value = 0
        score = 0
    
    data = {}
    data['average response'] = average_response
    data['minimum'] = min_value
    data['maximum'] = max_value
    data['score'] = score
    
    print(data)

    # %% make dynamic filename and write JSON

    now: tuple[int] = time.localtime()

    now_str = "-".join(map(str, now[:3])) + "T" + "_".join(map(str, now[3:6]))
    filename = f"score-{now_str}.json"

    print("write", filename)

    write_json(filename, data)
    ufirestore.create(document_path, filename, document_id=None, bg=True, cb=None)

if __name__ == "__main__":
    # using "if __name__" allows us to reuse functions in other script files

    led = Pin(17, Pin.OUT) #setting LED pin to output
    button = Pin(16, Pin.IN, Pin.PULL_UP) #setting button pin to input

    t: list[int | None] = []

    blinker(3, led)

    for i in range(N):
        time.sleep(random_time_interval(0.5, 5.0))

        led.high()

        tic = time.ticks_ms()#start time
        t0 = None
        while time.ticks_diff(time.ticks_ms(), tic) < on_ms:#diff between start time and cur time less than length of light pulse(else we missed the light)
            if button.value() == 0:#does this mean if button clicked value = 0?
                t0 = time.ticks_diff(time.ticks_ms(), tic)#when button clicked t0 stores time diff (as lomng as light is still on)
                led.low()
                break
        t.append(t0)#t is list holding all press times, report average min and max after this loop

        led.low()
    #it should have flashed 10 times and all valid inputs in t, calc average and min and maxin scorer:

    blinker(5, led)

    scorer(t)# this function adapted to report avg min and max.
