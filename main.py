import requests
import time
import yagmail

def sendEmail():
    print("Sending an email...")
    yag = yagmail.SMTP(FROM, 'pass')
    yag.send(TO, SUBJECT, TEXT)
    return

while True:
    response = requests.get('https://ubc-courses-api.herokuapp.com/2018W/CPSC/310/L1F')
    remainingSeats = response.json()['totalRemaining']
    if (remainingSeats > 0):
        print("Total seats currently remaining: " + str(remainingSeats))
        sendEmail()
    time.sleep(10)
