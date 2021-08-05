import json
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium_stealth import stealth
import undetected_chromedriver.v2 as uc

import email_code

outlook_accounts = []


class Automate:
    def run(self, account_number):
        chrome_options = uc.ChromeOptions()
        chrome_options.add_argument('--user-data-dir=c:\\temp\\profile2')
        chrome_options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
        driver = uc.Chrome(options=chrome_options)
        with driver:
            driver.get('https://www.epicgames.com/id/register/epic')
        stealth(driver,
                languages=["ru-RU", "ru"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )
        driver.implicitly_wait(10)
        if driver.current_url == 'https://www.epicgames.com/id/register/date-of-birth':
            elem = driver.find_element_by_xpath('//div[text()=\"ДД\"]').click()
            day = outlook_accounts[str(account_number)]['day']
            elem = driver.find_element_by_xpath(f'//li[text()=\"{day}\"]').click()
            elem = driver.find_element_by_xpath('//div[text()=\"ММ\"]').click()
            elem = driver.find_element_by_xpath('//li[text()=\"май\"]').click()
            elem = driver.find_element_by_id('year')
            elem.send_keys(outlook_accounts[str(account_number)]['year'])
            elem = driver.find_element_by_id("continue").click()
        driver.implicitly_wait(10)
        elem = driver.find_element_by_name('name')
        elem.send_keys(str(outlook_accounts[str(account_number)]['name']))
        elem = driver.find_element_by_name('lastName')
        elem.send_keys(str(outlook_accounts[str(account_number)]['lastname']))
        elem = driver.find_element_by_name('displayName')
        elem.send_keys(str(outlook_accounts[str(account_number)]['username']))
        elem = driver.find_element_by_name('email')
        elem.send_keys(str(outlook_accounts[str(account_number)]['email']))
        elem = driver.find_element_by_name('password')
        elem.send_keys(str(outlook_accounts[str(account_number)]['password']))
        elem = driver.find_element_by_name('tos').click()
        sleep(1)
        elem = driver.find_element_by_id('btn-submit').click()
        driver.implicitly_wait(1000)
        elem = driver.find_element_by_id("email-verify-label")
        sleep(20)
        code = email_code.get_code(str(outlook_accounts[str(account_number)]['email']))
        driver.implicitly_wait(5)
        for i in range(0, 6):
            elem = driver.find_element_by_name(f"code-input-{i}")
            elem.send_keys(code[i])
        sleep(1)
        driver.find_element_by_id("continue").click()

        with open('epic_accounts.txt', 'a') as epic_list:
            epic_list.write(str(outlook_accounts[str(account_number)]['email']) + '\n')
        driver.close()
        driver.quit()

    def __init__(self):
        epic_accounts = []
        with open('epic_accounts.txt', 'r') as epic_list:
            epic_accounts = epic_list.readlines()
            epic_accounts = [string.rstrip() for string in epic_accounts]
        for j in range(len(outlook_accounts)):
            if outlook_accounts[str(j)]['email'] not in epic_accounts:
                self.run(j)


def main():
    output_file = str(input("Введите название файла >>> "))
    if '.json' in output_file:
        output_file = output_file[:-5]
    with open(output_file + '.json') as json_outlook:
        global outlook_accounts
        outlook_accounts = json.loads(json_outlook.read())
    Automate()


if __name__ == "__main__":
    main()
