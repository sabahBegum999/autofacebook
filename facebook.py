from selenium import webdriver
from getpass import getpass
import pyautogui
import time
from time import sleep

#code to auto login 
username = input("enter your username")
password = getpass("Enter your password: ")

driver = webdriver.Chrome("C:\\webdriver\\chromedriver.exe")
driver.get("https://www.facebook.com/")

username_textbox = driver.find_element_by_id("email")
username_textbox.send_keys(username)
password_textbox = driver.find_element_by_id("pass")
password_textbox.send_keys(password)

login_button = driver.find_element_by_id("u_0_3")
login_button.submit()

#code to auto comment
comments = ["hi","just commenting for fun","I love python programming","Python comment"]
time.sleep(5)
for i in range(5):
    pyautogui.typewrite(comments[i%4])
    pyautogui.typewrite("\n")
    time.sleep(2)

#code  to add friends
def acceptFriendRequest():
        friend_requests_button = driver.find_element_by_id("fbRequestsJewel")
        friend_requests_button.click()
        sleep(4)
        request_box = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div[2]/div[1]/div/div/ul/li/div/div/div[1]/div[1]/div/div/div[2]")
        buttons_to_confirm_request = request_box.find_elements_by_name("actions[accept]")
        request_list = [i.text for i in buttons_to_confirm_request if i.text != '']
        i = 0 
        while (i<len(request_list)):
            buttons_to_confirm_request[i].click()
            sleep(1)
            # driver.execute_script("window.scrollBy(0,75)",request_box)
            sleep(1)
            i+=1

acceptFriendRequest()   

#code to post facebook status
postarea = driver.find_element_by_class_name('_5qtp')
postarea.click()
sleep(3)
activepostarea = driver.switch_to_active_element()
activepostarea("Hello World")
postbtn = driver.find_elements_by_tag_name('button')
for btn in postbtn:
    if btn.text=='Post':
        btn.click()



