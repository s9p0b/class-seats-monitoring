import requests
import time
import smtplib
import argparse
parser = argparse.ArgumentParser()

parser.add_argument("-e", "--email", help="Sender Email")
parser.add_argument("-p", "--password", help="Password")
parser.add_argument("-t", "--toemail", help="Receiver Email")
parser.add_argument("-d", "--dept", help="Course Department")
parser.add_argument("-n", "--num", help="Course Number")
parser.add_argument("-s", "--section", help="Course Section")

args = parser.parse_args()
skip = True

for arg in vars(args):
    if not getattr(args, arg):
        skip = False

if not skip:
    args.email = input('Sender Email: ')
    args.password = input('Password: ')
    args.toemail = input('Receiver Email: ')
    args.dept = input('Course Department: ')
    args.num = input('Course Number: ')
    args.section = input('Course Section: ')


def sendEmail():
    print("Sending an email...")
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(args.email, args.password)
    subject = args.dept + args.num + " " + args.section + ": FREE SEAT"
    content = "Free seats avaliable for " + args.dept + args.num + " " + args.section
    message = 'Subject: {}\n\n{}'.format(subject, content)
    server.sendmail(
        args.email,
        args.toemail,
        message)
    server.quit()
    print("Done")


def main():
    while True:
        response = requests.get(
            'https://ubc-courses-api.herokuapp.com/2019W/' + args.dept +  '/' + args.num + '/' + args.section)
        remainingSeats = response.json()['totalRemaining']
        if (remainingSeats > 0):
            print("Total seats currently remaining: " + str(remainingSeats))
            sendEmail()
            return
        else:
            print("The class is full :c")
        time.sleep(60)


main()