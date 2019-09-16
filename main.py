import requests
import time

while True:
    response = requests.get('https://ubc-courses-api.herokuapp.com/2018W/CPSC/310/L1F')
    remainingSeats = response.json()['totalRemaining']
    if (remainingSeats > 0):
        print("Total seats currently remaining: " + str(remainingSeats))
    time.sleep(10)
