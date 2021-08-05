from time import sleep

from selenium_stealth import stealth
import undetected_chromedriver.v2 as uc

epic_accounts = []


class Automate:
    def run(self, account_number) -> None:
        chrome_options = uc.ChromeOptions()
        chrome_options.add_argument('--user-data-dir=c:\\temp\\profile2')
        chrome_options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
        driver = uc.Chrome(options=chrome_options)
        driver.get("https://www.epicgames.com/id/login/epic")
        stealth(driver,
                languages=["ru-RU", "ru"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )
        driver.implicitly_wait(5)
        driver.implicitly_wait(10)
        driver.find_element_by_id("email").send_keys(str(epic_accounts[account_number]))
        driver.find_element_by_id("password").send_keys("PASSr544bb1")
        driver.find_element_by_id("rememberMe").click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//button[@type="submit"]').click()
        input('f ')
        with open('nitro_accs.txt', 'a') as accs_nitro:
            accs_nitro.write(str(epic_accounts[account_number]) + '\n')
        driver.close()
        driver.quit()

    def __init__(self):
        global epic_accounts
        with open("nitro_accs.txt", 'r') as nitro_list:
            nitro_accs = nitro_list.readlines()
            for j in range(len(epic_accounts)):
                if epic_accounts[j] not in nitro_accs:
                    self.run(j)


def main():
    global epic_accounts
    output_file = str(input("Введите название файла >>> "))
    if '.txt' not in output_file:
        output_file += '.txt'
    with open(output_file, 'r') as epic_list:
        epic_accounts = epic_list.readlines()
        epic_accounts = [string.rstrip() for string in epic_accounts]

    Automate()


if __name__ == "__main__":
    main()
