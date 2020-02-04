from selenium import webdriver
from credentials import username,password
from time import sleep

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com')

        sleep(5)

        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button')
        fb_btn.click()

        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(bot.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)
        pass_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pass_in.send_keys(password)
        log_in = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        log_in.click()

        self.driver.switch_to_window(base_window)

        sleep(2)

        popup1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup1.click()

        sleep(2)

        popup2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup2.click()


    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
        like_btn.click()

    def close_match(self):
        keep_swipebtn = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        keep_swipebtn.click()

    def close_popup(self):
        self.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]').click()


    def auto_swipe(self):
        while True:
            sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_match()
                except Exception:
                    self

bot = TinderBot()
bot.login()
bot.auto_swipe()