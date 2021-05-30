#import requests to handle pulling from the openweathermap API, Import Json in order to filter the get request into the specific information we need
import requests, json
# Yagmail is an easy way for you to send emails from a python script, compared to using a gmail API. Keyring enables you to keep your username and password for your account secure, encrypted, and out of your script
import yagmail, keyring
# Schedule is what we use to enable the script to run every day at 12:38. 
import schedule
import time
#
# The actual GET request, defined by Notification to allow for schedule to work properly. Yagmail sends the notification through a MMS gateway as a text message, just from an email.
def Notification():
    response = requests.get( "https://api.openweathermap.org/data/2.5/onecall?lat=36.5298&lon=-87.3595&units=imperial&exclude=minutely,hourly,current,alerts&appid=[YourAppID]" )
    appid = ["YourAPPID"]
    Temperature = (response.json().get('daily')[0].get('temp').get('min'))
    Textmessage = str(Temperature)
    Temperature_alert = 80
    if Temperature < Temperature_alert:
        yagmail.SMTP('Yourgmail@gmail.com').send('1234567890@examplegateway.com', '[your title]',"Hi Tjrm710, The low for today will be "+ Textmessage +"°F, Stay cool!")
#
#
# Schedules the program to run at a set time every single day
schedule.every().day.at("12:38").do(Notification)
while True:
    schedule.run_pending()
    time.sleep(1)
