from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

URL = 'https://selfregistration.cowin.gov.in/'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0)'
                         ' Gecko/20100101 Firefox/73.0'}


def get_to_OTP_screen(phone_number):
    options = webdriver.ChromeOptions()

    options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    try:
        chrome_driver_binary = r"chromedriver.exe"
        web = webdriver.Chrome(chrome_driver_binary, options=options)
    except:
        web = webdriver.Chrome(ChromeDriverManager().install())

    web.get(URL)

    time.sleep(2)

    mob_number = phone_number
    mob_field = web.find_element_by_xpath('//*[@id="mat-input-0"]')
    mob_field.send_keys(mob_number)

    submit1 = web.find_element_by_xpath('//*[@id="main-content"]/app-login/ion-content/div/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[1]/ion-grid/form/ion-row/ion-col[2]/div/ion-button')
    submit1.click()

    user_choice = input('\nPlease click ENTER button to close application')
    if not user_choice:
        print("ABORTED")
        quit()
