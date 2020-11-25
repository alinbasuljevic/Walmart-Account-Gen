from selenium import webdriver
import discord, random, names, requests, time
import requests

def account_creation(driver, name, email, domain, password):
    if name == '':  
        first_name = names.get_first_name()
        last_name = names.get_last_name()
    else:
        first_name = name.split(' ')[0]
        last_name = name.split(' ')[1]
        pass
        
    email_final = '{}+{}{}'.format(email, random.randint(0,10000), domain)
    driver.get('https://www.walmart.com/account/signup?ref=domain')
    first_step = driver.find_element_by_xpath('//*[@id="first-name-su"]').send_keys(first_name)
    second_step = driver.find_element_by_xpath('//*[@id="last-name-su"]').send_keys(last_name)
    third_step = driver.find_element_by_xpath('//*[@id="email-su"]').send_keys(email_final)
    fourth_step = driver.find_element_by_xpath('//*[@id="password-su"]').send_keys(password)
    checkbox = driver.find_element_by_xpath('//*[@id="sign-up-form"]/div[6]/label').click()
    create_button = driver.find_element_by_xpath('//*[@id="sign-up-form"]/button[1]').click()
    time.sleep(10)
    if driver.current_url == 'https://www.walmart.com/account/?action=Create&rm=true':
        print ('SUCCESSFULLY GENERATED ACCOUNT: {}|{}'.format(email_final, password))
        driver.quit()
    else:
        print ('FAILED CREATION: {}|{}'.format(email, password))
        driver.quit()
    

if __name__ == '__main__':
    main_menu = input('Random Names [1] or Static Name [2]: ')
    if main_menu == '2':
        name = input('Enter Full Name (ex. Test Guy): ')
        email =  input('Enter Email Prefix: ')
        domain = input('Enter Domain (ex. @gmail.com): ')
        password = input('Enter Password: ')
        while True:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
            driver = webdriver.Chrome(options=chrome_options, executable_path="C:\\Users\\Alin Basuljevic\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")
            account_creation(driver, name, email, domain, password)
    else:
        name = ''
        email = input('Enter Email Prefix: ')
        domain = input('Enter Domain (ex. @gmail.com): ')
        password = input('Enter Password: ')
        while True:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
            driver = webdriver.Chrome(options=chrome_options, executable_path="C:\\Users\\Alin Basuljevic\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")
            account_creation(driver, name, email, domain, password)
    
    
