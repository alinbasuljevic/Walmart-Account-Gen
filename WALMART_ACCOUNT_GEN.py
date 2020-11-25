from selenium import webdriver
import discord, random, names
from discord_webhook import DiscordWebhook, DiscordEmbed
import requests
import time
from bs4 import BeautifulSoup as bs

def account_creation(driver):
    first_name = names.get_first_name()
    last_name = names.get_last_name()
    email = 'test+{}@gmail.com'.format(random.randint(0,1000))
    password = 'createdbyalin123'
    driver.get('https://www.walmart.com/account/signup?ref=domain')
    first_step = driver.find_element_by_xpath('//*[@id="first-name-su"]').send_keys(first_name)
    second_step = driver.find_element_by_xpath('//*[@id="last-name-su"]').send_keys(last_name)
    third_step = driver.find_element_by_xpath('//*[@id="email-su"]').send_keys(email)
    fourth_step = driver.find_element_by_xpath('//*[@id="password-su"]').send_keys(password)
    checkbox = driver.find_element_by_xpath('//*[@id="sign-up-form"]/div[6]/label').click()
    create_button = driver.find_element_by_xpath('//*[@id="sign-up-form"]/button[1]').click()
    time.sleep(10)
    if driver.current_url == 'https://www.walmart.com/account/?action=Create&rm=true':
        print ('SUCCESSFULLY GENERATED ACCOUNT: {}|{}'.format(email, password))
        driver.quit()
    else:
        print ('FAILED CREATION: {}|{}'.format(email, password))
        driver.quit()
    

if __name__ == '__main__':
    while True:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        driver = webdriver.Chrome(options=chrome_options, executable_path="C:\\Users\\Alin Basuljevic\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")
        account_creation(driver)
    
    
