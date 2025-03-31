from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time
from datetime import datetime
import string
import requests
import os

now = datetime.now()

BirthMonthList = {
    1 : '//*[@id="MonthDropdown"]/option[2]',
    2 : '//*[@id="MonthDropdown"]/option[3]',
    3 : '//*[@id="MonthDropdown"]/option[4]',
    4 : '//*[@id="MonthDropdown"]/option[5]',
    5 : '//*[@id="MonthDropdown"]/option[6]',
    6 : '//*[@id="MonthDropdown"]/option[7]',
    7 : '//*[@id="MonthDropdown"]/option[8]',
    8 : '//*[@id="MonthDropdown"]/option[9]',
    9 : '//*[@id="MonthDropdown"]/option[10]',
    10 : '//*[@id="MonthDropdown"]/option[11]',
    11 : '//*[@id="MonthDropdown"]/option[12]',
    12 : '//*[@id="MonthDropdown"]/option[13]'
}
BirthDayList = {
    1 : '//*[@id="DayDropdown"]/option[2]',
    2 : '//*[@id="DayDropdown"]/option[3]',
    3 : '//*[@id="DayDropdown"]/option[4]',
    4 : '//*[@id="DayDropdown"]/option[5]',
    5 : '//*[@id="DayDropdown"]/option[6]',
    6 : '//*[@id="DayDropdown"]/option[7]',
    7 : '//*[@id="DayDropdown"]/option[8]',
    8 : '//*[@id="DayDropdown"]/option[9]',
    9 : '//*[@id="DayDropdown"]/option[10]',
    10 : '//*[@id="DayDropdown"]/option[11]',
    11 : '//*[@id="DayDropdown"]/option[12]',
    12 : '//*[@id="DayDropdown"]/option[13]',
    13 : '//*[@id="DayDropdown"]/option[14]',
    14 : '//*[@id="DayDropdown"]/option[15]',
    15 : '//*[@id="DayDropdown"]/option[16]',
    16 : '//*[@id="DayDropdown"]/option[17]',
    17 : '//*[@id="DayDropdown"]/option[18]',
    18 : '//*[@id="DayDropdown"]/option[19]',
    19 : '//*[@id="DayDropdown"]/option[20]',
    20 : '//*[@id="DayDropdown"]/option[21]',
    21 : '//*[@id="DayDropdown"]/option[22]',
    22 : '//*[@id="DayDropdown"]/option[23]',
    23 : '//*[@id="DayDropdown"]/option[24]',
    24 : '//*[@id="DayDropdown"]/option[25]',
    25 : '//*[@id="DayDropdown"]/option[26]',
    26 : '//*[@id="DayDropdown"]/option[27]',
    27 : '//*[@id="DayDropdown"]/option[28]',
    28 : '//*[@id="DayDropdown"]/option[29]',
    29 : '//*[@id="DayDropdown"]/option[30]',
    30 : '//*[@id="DayDropdown"]/option[31]',
    31 : '//*[@id="DayDropdown"]/option[32]',
}
BirthYearList = {
    1 : '//*[@id="YearDropdown"]/option[32]', # 1990
    2 : '//*[@id="YearDropdown"]/option[31]', # 1991
    3 : '//*[@id="YearDropdown"]/option[30]', # 1992
    4 : '//*[@id="YearDropdown"]/option[29]', # 1993
    5 : '//*[@id="YearDropdown"]/option[28]', # 1994
    6 : '//*[@id="YearDropdown"]/option[27]', # 1995
    7 : '//*[@id="YearDropdown"]/option[26]', # 1996
    8 : '//*[@id="YearDropdown"]/option[25]', # 1997
    9 : '//*[@id="YearDropdown"]/option[24]', # 1998
    10 : '//*[@id="YearDropdown"]/option[23]', # 1999
    11 : '//*[@id="YearDropdown"]/option[22]', # 2000
    12 : '//*[@id="YearDropdown"]/option[21]', # 2001
    13 : '//*[@id="YearDropdown"]/option[20]', # 2002
    14 : '//*[@id="YearDropdown"]/option[19]', # 2003
    15 : '//*[@id="YearDropdown"]/option[18]', # 2004
    16 : '//*[@id="YearDropdown"]/option[17]', # 2005
    17 : '//*[@id="YearDropdown"]/option[16]', # 2006
    18 : '//*[@id="YearDropdown"]/option[15]', # 2007
}
GenderList = {
    1 : '//*[@id="FemaleButton"]',
    2 : '//*[@id="MaleButton"]'
}
Names = [
    'Lily', 'Lucas', 'Penelope', 'Jaxon', 'Ezra', 'Amelia', 'Emily', 'Grace', 'Penelope', 'Avery', 'Chloe',
    'Evelyn', 'Michael', 'Matthew', 'Isaiah', 'Amelia', 'Zoe', 'Aurora', 'Evelyn', 'Zoe', 'Elijah', 'Ryan', 'Emily', 
    'William', 'Sophia', 'Ruby', 'Mia', 'Victoria', 'Elena', 'Aurora', 'Grayson', 'Lily', 'Elena', 'Peyton', 'Avery', 
    'Emmett', 'Joshua', 'Carter', 'Lily', 'Eleanor', 'Willow', 'Lucy', 'Grayson', 'Audrey', 'Ava', 'Zoe', 'Sophia', 
    'Henry', 'Liam', 'Michael', 'Avery', 'Daniel', 'Zoe', 'Lincoln', 'Maya', 'Lucas', 'Adeline', 'Grace', 'Eleanor', 
    'Audrey', 'Julian', 'Maya', 'Jack', 'Madeline', 'Elena', 'Victoria', 'Josie', 'Mason', 'Audrey', 'Harper', 'Levi', 
    'Ella', 'Camila', 'Emily', 'William', 'Charlotte', 'Joshua', 'Sophia', 'Theo', 'Daniel', 'Theo', 'Scarlett', 'Scarlett', 
    'Henry', 'Charlotte', 'Adeline', 'Josie', 'Olivia', 'Hailey', 'Grace', 'Aidan', 'Sophia', 'Zoe', 'Sara', 'Gabriel', 
    'Gabriel', 'Penelope', 'Daniel', 'Audrey', 'Kai', 'Miles', 'Xander', 'Levi', 'Olivia', 'Liam', 'Lucas', 'Aurora', 'Lily', 
    'Harper', 'Mia', 'David', 'Finn', 'Audrey', 'Daniel', 'Hailey', 'Avery', 'Lucas', 'Daniel', 'Ruby', 'Maya', 'Sara', 'Liam', 
    'Daniel', 'Hazel', 'Lucas', 'Ruby', 'Levi', 'Ryan', 'Kai', 'Xander', 'Scarlett', 'Lucas', 'Nate', 'Isaiah', 'Aria', 'Samuel', 
    'Savannah', 'Hailey', 'Michael', 'Sara', 'Willow', 'John', 'Aria', 'Lincoln', 'Samuel', 'Alex', 'Isabella', 'Xander', 'Chloe', 
    'Emilia', 'Hailey', 'Ethan', 'Sophia', 'Zoe', 'Lucas', 'Grace', 'Finn', 'Bella', 'Jacob', 'Jacob', 'Charlie', 'Aurora', 'Nate', 
    'Oliver', 'Victoria', 'Carter', 'Owen', 'Logan', 'Gavin', 'Daniel', 'Maya', 'John', 'Savannah', 'Hazel', 'Theo', 'Sara', 'Joseph', 
    'Ezra', 'Harper', 'Elijah', 'Avery', 'Liam', 'Lincoln', 'Sophia', 'Charlotte', 'Daniel', 'Alice', 'Adeline', 'William', 'Joseph', 
    'Scarlett', 'Nora', 'Mackenzie', 'Zoe', 'Grace', 'Eva', 'Joshua', 'Aidan', 'Gavin', 'Finn', 'Hailey', 'Charlotte', 'Audrey', 'Ella', 
    'Caleb', 'Ella', 'Eva', 'Gavin', 'Finn', 'James', 'Landon', 'Luna', 'Zoe', 'Asher', 'Peyton', 'Cora', 'Lincoln', 'Gavin', 'Mason', 
    'Kai', 'Aidan', 'Layla', 'Lincoln', 'Henry', 'Gabriel', 'Scarlett', 'Jacob', 'Julian', 'Madison', 'Emmett', 'William', 'Miles', 
    'Bella', 'Alex', 'Chloe', 'Sadie', 'Victoria', 'Caleb', 'Lily', 'Sophie', 'Audrey', 'Madison', 'Maya', 'Sara', 'Nate', 'Peyton', 
    'Harper', 'Nathan', 'Charlotte', 'Sadie', 'David', 'Amelia', 'Emilia', 'Isabella', 'Sophie', 'Isaac', 'Joshua', 'John', 'Avery', 
    'Mia', 'Ryan', 'Cooper', 'Logan', 'Gabriel', 'Aidan', 'Nathan', 'Eli', 'Sophie', 'Jack', 'Landon', 'Charlotte', 'Alexander', 'Madeline', 
    'Isaac', 'Logan', 'Matthew', 'Cora', 'William', 'Cooper', 'Gabriel', 'Lucas', 'Kinsley', 'Isaiah', 'Nathan', 'Elijah', 'Ryan', 'Cora', 
    'Hailey', 'Caleb', 'Ella', 'Nora', 'Luna', 'Avery', 'Cora', 'Harper', 'Scarlett', 'Eva', 'Layla', 'Matthew', 'Emmett', 'Xander', 'Cora', 
    'Miles', 'Lincoln', 'Scarlett', 'Lucas', 'Audrey', 'Amelia', 'Eleanor', 'Scarlett', 'Ella', 'Kai', 'Sophie', 'Mia', 'Nolan', 'Alice', 'Cora', 
    'Isaac', 'Isabella', 'Charlotte', 'Charlie', 'Charlotte', 'Ruby', 'Ryan', 'Sophia', 'Finn', 'Sadie', 'Scarlett', 'Sara', 'Kinsley', 'Benjamin', 
    'Cora', 'Benjamin', 'Caleb', 'Caleb', 'Xander', 'Penelope', 'Scarlett', 'Cooper', 'Jaxon', 'Julian', 'Emily', 'Dylan', 'Maya', 'Matthew', 
    'Victoria', 'Kai', 'Chloe', 'Peyton', 'Daniel', 'Elijah', 'Gavin', 'Nora', 'Liam', 'James', 'Joshua', 'Amelia', 'Lucy', 'Audrey', 'William', 
    'Sebastian', 'Evelyn', 'Camila', 'Maya', 'Bella', 'Samuel', 'Lucas', 'Lucas', 'Lily', 'Amelia', 'Lucy', 'Isaiah', 'Kinsley', 'Levi', 'Lily', 
    'Aidan', 'Ella', 'Mason', 'Benjamin', 'Gianna', 'Lucas', 'Julian', 'Lucas', 'Owen', 'Benjamin'
]

class AutoACC():
    def __init__(self,user=None,passwd=None,url=None):
        self.user = user
        self.passwd = passwd
        self.url = url
    def CreateRandomACC(self):
        letters = string.ascii_uppercase
        digits = string.digits
        passwd = ''.join(random.choices(letters, k=2))
        passwd += ''.join(random.choices(digits, k=3))
        passwd += ''.join(random.choices(letters, k=4))
        passwd += ''.join(random.choices(letters, k=2))
        passwd += ''.join(random.choices(digits, k=3))

        BirthMonthListRandom = random.randint(1,len(BirthMonthList))
        BirthDayListRandom = random.randint(1,len(BirthDayList))
        BirthYearListRandom = random.randint(1,len(BirthYearList))
        GenderListRandom = random.randint(1,len(GenderList))
        NamesRandom = random.randint(1,len(Names))
        BackNumber = random.randint(000000000,999999999)

        driver = webdriver.Chrome()
        driver.get('https://www.roblox.com/')

        button = driver.find_element(By.XPATH, value=BirthMonthList[BirthMonthListRandom]) # month
        button.click()
        print(f"[{now.hour}:{now.minute}:{now.second}] [$] STATUS : BirthMonthList={BirthMonthList[BirthMonthListRandom]}")
        button = driver.find_element(By.XPATH, value=BirthDayList[BirthDayListRandom]) # day
        button.click()
        print(f"[{now.hour}:{now.minute}:{now.second}] [$] STATUS : BirthDayList={BirthDayList[BirthDayListRandom]}")
        button = driver.find_element(By.XPATH, value=BirthYearList[BirthYearListRandom]) # year
        button.click()
        print(f"[{now.hour}:{now.minute}:{now.second}] [$] STATUS : BirthYearList={BirthYearList[BirthYearListRandom]}")
        button = driver.find_element(By.XPATH, value=GenderList[GenderListRandom]) # gender
        button.click()
        print(f"[{now.hour}:{now.minute}:{now.second}] [$] STATUS : GenderList={GenderList[GenderListRandom]}")

        text_box = driver.find_element(By.XPATH, '//*[@id="signup-username"]') 
        text_box.send_keys(f'{Names[NamesRandom]}{BackNumber}') # name
        print(f"[{now.hour}:{now.minute}:{now.second}] [$] STATUS : Names={Names[NamesRandom]}{BackNumber}")

        text_box = driver.find_element(By.XPATH, '//*[@id="signup-password"]') 
        text_box.send_keys(f'{passwd}') # password
        print(f"[{now.hour}:{now.minute}:{now.second}] [$] STATUS : Password={passwd}")

        button = driver.find_element(By.XPATH, value='//*[@id="signup-button"]') # SignUp
        button.click()

        time.sleep(5)

        cookies = driver.get_cookies()
        AccCookie = cookies[-1]['value'].split("_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_")[1]
        
        result = f"{Names[NamesRandom]}{BackNumber}:{passwd}:{AccCookie}"

        time.sleep(20000)
        driver.quit()


    def getCookie(self):
        driver = webdriver.Chrome()
        driver.get('https://www.roblox.com/login')

        text_box = driver.find_element(By.XPATH, '//*[@id="login-username"]') 
        text_box.send_keys(f'{self.user}') # name
        print(f"[{now.hour}:{now.minute}:{now.second}] [$] STATUS : Names={self.user}")

        text_box = driver.find_element(By.XPATH, '//*[@id="login-password"]') 
        text_box.send_keys(f'{self.passwd}') # password
        print(f"[{now.hour}:{now.minute}:{now.second}] [$] STATUS : Password={self.passwd}") 

        button = driver.find_element(By.XPATH, value='//*[@id="login-button"]') # LogIn
        button.click()

        time.sleep(5)
        
        cookies = driver.get_cookies()
        for cookie in cookies:
            if cookie['name'] == '.ROBLOSECURITY':
                print(f"{cookie['value'].split("_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_")[1]}")

        time.sleep(20000)

    def AccFollower(self):
        driver = webdriver.Chrome()
        driver.get(self.url) 
        CookieFromStorageList = []
        with open("AccountStorage.txt", "r", encoding="utf-8") as file:
            for line in file:
                CookieFromStorage = line.split(":")[2]

                cookie = {
                    'name': '.ROBLOSECURITY',
                    'value': CookieFromStorage # ///// Error IS HERE !!!!!! /////
                }
                print(cookie['value'])
                driver.add_cookie(cookie)
                driver.refresh()
                
                time.sleep(2)
                button = driver.find_element(By.XPATH, value='//*[@id="user-agreements-checker-modal"]/div/div/div[3]/div[2]/button') # igree button (if have notification if not YOU CAN DELETE THIS)
                button.click() # This too
                time.sleep(1) # This too
                button = driver.find_element(By.XPATH, value='//*[@id="profile-header-container"]/div/div[3]/button[2]') # open dropdown
                button.click()
                time.sleep(1)
                button = driver.find_element(By.XPATH, value='//*[@id="follow-button"]') # Follow2
                button.click()

                time.sleep(10)

# If you want to Create RB ACC Just call function -> auto_acc.AutoACC().CreateRandomACC()
#
#
# If you want to Get Cookie fast way then call function -> auto_acc.AutoACC(user="YOUR_USERNAME",passwd="YOUR_PASSWORD").getCookie()
#
#
# If you want more roblox ACC follower then call function -> auto_acc.AutoACC(url=YOUR_ACCOUNT_LINK_PROFILE).AccFollower()   
# # (Error at cookie setting IDK why, I think it error at variable or datatype or maybe it error at space text)
#
#
#
# (┬┬﹏┬┬) (┬┬﹏┬┬) (┬┬﹏┬┬) (┬┬﹏┬┬) (┬┬﹏┬┬) ===== WARNING WARNING ===== (┬┬﹏┬┬) (┬┬﹏┬┬) (┬┬﹏┬┬) (┬┬﹏┬┬) (┬┬﹏┬┬)
# (┬┬﹏┬┬) (┬┬﹏┬┬) (┬┬﹏┬┬) (┬┬﹏┬┬) ===== WARNING WARNING ===== (┬┬﹏┬┬) (┬┬﹏┬┬) (┬┬﹏┬┬) (┬┬﹏┬┬) (┬┬﹏┬┬)
# (┬┬﹏┬┬) (┬┬﹏┬┬) (┬┬﹏┬┬) ===== WARNING WARNING ===== (┬┬﹏┬┬) (┬┬﹏┬┬) (┬┬﹏┬┬) (┬┬﹏┬┬) (┬┬﹏┬┬)
# (┬┬﹏┬┬) (┬┬﹏┬┬) ===== WARNING WARNING ===== (┬┬﹏┬┬) (┬┬﹏┬┬) (┬┬﹏┬┬) (┬┬﹏┬┬) (┬┬﹏┬┬)
# (┬┬﹏┬┬) ===== WARNING WARNING ===== (┬┬﹏┬┬) (┬┬﹏┬┬) (┬┬﹏┬┬) (┬┬﹏┬┬) (┬┬﹏┬┬)
# ===== WARNING WARNING ===== (┬┬﹏┬┬) (┬┬﹏┬┬) (┬┬﹏┬┬) (┬┬﹏┬┬) (┬┬﹏┬┬)
#   ===== WARNING WARNING ===== (┬┬﹏┬┬) (┬┬﹏┬┬) (┬┬﹏┬┬) (┬┬﹏┬┬)
#       ===== WARNING WARNING ===== (┬┬﹏┬┬) (┬┬﹏┬┬) (┬┬﹏┬┬)
#           ===== WARNING WARNING ===== (┬┬﹏┬┬) (┬┬﹏┬┬)
#               ===== WARNING WARNING ===== (┬┬﹏┬┬)
#                   ===== WARNING WARNING =====
#                   ===== WARNING WARNING =====
#                   ===== WARNING WARNING =====
#                   ===== WARNING WARNING =====
#                   ===== WARNING WARNING =====
#                   ===== WARNING WARNING =====
#
#
#
#
#               1. I HAVE NO BYPASS (The first and second function)
#
#
#               2. I lazy to fix cookie error cause of variable (I THINK YOU CAN FIX IT.) (thrid function)