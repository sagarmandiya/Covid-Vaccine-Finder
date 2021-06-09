import os
import requests
import time
from playsound import playsound
from OpenWebBrowser import get_to_OTP_screen


def VaccineFinder(phone_number, min_age_limit):
    flag = 0
    result = requests.get(URL, headers=header)
    result_json = result.json()
    sessions = result_json["sessions"]
    for data in sessions:
        if((data["available_capacity"] > 0) & (data["min_age_limit"] == min_age_limit)):
            flag += 1
            print('Slot Found!!\n')
            print('Venue:', data["name"])
            print('Pincode:', data["pincode"])
            print('Vaccine:', data["vaccine"])
            print('Quantity:', data["available_capacity"])
            playsound('sounds/alarm.wav')
            if phone_number != 987654321:
                print('\nOpening Web Browser\n')
                get_to_OTP_screen(phone_number)
            return True
    if(flag == 0):
        global counter
        counter += 1
        print("Vaccine slots are not yet available. Checked:", counter, 'times. ')
        return False


if __name__ == "__main__":
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

    pincode = 452001  # Your Pincode here
    date = '10-06-2021'  # Date on which to find open slots
    min_age_limit = 18  # Age group of which the vaccine slot to be found i.e., 18 or 45
    refresh_time = 10  # checking the slots every 10 seconds

    try:
        print('Entering the phone number will automatically, open up chrome browser and send OTP on your mobile when the slot is found, but you can skip this step by simply pressing ENTER ')
        phone_number = int(input('Enter Mobile number: '))
    except:
        phone_number = 987654321


    global counter
    counter = 0

    URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}'.format(pincode, date)

    while(VaccineFinder(phone_number, min_age_limit) != True):
        time.sleep(refresh_time)
        os.system('cls')
