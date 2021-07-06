
from selenium import webdriver


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

file = open('AutoInformaion.txt', 'r')
f = file.readlines()

newList = []
for line in f:
    newList.append(line.strip())

newList.reverse()


class Bot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def findform(self):


        self.driver.get('https://forms.gle/qTiqCCMENjsCb9pF9')

        name = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        name.click()
        name.send_keys(newList.pop())

        email = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        email.click()
        email.send_keys(newList.pop())

        address = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')
        address.click()
        address.send_keys(newList.pop())

        phonenumber = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
        phonenumber.click()
        phonenumber.send_keys(newList.pop())

        comments = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]/textarea')
        comments.click()
        comments.send_keys(newList.pop())

        submit = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
        submit.click()


bot = Bot()


while len(newList):
    bot.findform()





