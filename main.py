
from selenium import webdriver


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# File is opened and read line by line
file = open('AutoInformaion.txt', 'r')
f = file.readlines()

# A list is initialized with the information that will populate the forms
newList = []
# A new line is added line by line to newList
for line in f:
    newList.append(line.strip())

# List is reversed to ensure the form is populated correctly (As the data is entered Backward)
newList.reverse()


class Bot():

    # Chrome webdriver is initialized
    def __init__(self):
        self.driver = webdriver.Chrome()

    def findform(self):

        # Script is taken to Form

        self.driver.get('https://forms.gle/qTiqCCMENjsCb9pF9')

        # The Name section is found by the xpath, clicked on, and the information is entered
        # by taking it from the end of the newList

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

# While loop that continues to run the script until the newList is empty
while len(newList):
    bot.findform()





