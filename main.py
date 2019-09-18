import requests
import time
import smtplib

def sendEmail():
    print("Sending an email...")
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("", "")
    message = 'Subject: {}\n\n{}'.format("L1F: FREE SEAT", "Free seats avaliable for L1F")
    server.sendmail(
            "",
            "",
            message)
    server.quit()
    print("Done")

def main():
    while True:
        response = requests.get('https://ubc-courses-api.herokuapp.com/2019W/CPSC/310/L1F')
        remainingSeats = response.json()['totalRemaining']
        if (remainingSeats > 0):
            print("Total seats currently remaining: " + str(remainingSeats))
            sendEmail()
            return
        else:
            print("The class is full :c")
        time.sleep(60)

main()
