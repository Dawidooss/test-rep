class KontoIstnieje(Exception):
    pass
class BrakProxy(Exception):
    pass

from tabnanny import check
from timeit import repeat
import undetected_chromedriver as uc
uc.install()

from http.server import executable
import os
import colorama
from colorama import Fore, Style
import selenium
import time
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities    

import subprocess
import time
import requests
import pytest
import time
import json
import random
from bs4 import BeautifulSoup
import clipboard

delayTime = 2
audioToTextDelay = 10
filename = '1.mp3'
googleIBMLink = 'https://speech-to-text-demo.ng.bluemix.net/'

path = os.getcwd()

#Main
os.system("cls")
os.system('title ' + 'Interia  ^| Replit Account Generator ')
def logo():
    aio = Fore.CYAN +"""   
                        
╔════════════════════╗     ___           _                   _         
[D] Dawidooss#22356       |_ _|  _ __   | |_    ___   _ __  (_)   __ _ 
[O] blue.z.czatu#9999      | |  | '_ \  | __|  / _ \ | '__| | |  / _` |
[W] >Youtube<              | |  | | | | | |_  |  __/ | |    | | | (_| |
╚════════════════════╝    |___| |_| |_|  \__|  \___| |_|    |_|  \__,_|

                                                                                                                                                    
"""
    print(aio)


from selenium.webdriver import Chrome

options = uc.ChromeOptions()

driver = Chrome()
driver.set_window_size(1920, 1080)

logo()

time.sleep(1)

def check_exists_by_xpath(xpath):
    try:
        driver.find_element(by=By.XPATH, value=xpath)
    except NoSuchElementException:
        return False
    return True


def main():
    while True:
        try:
            domain = json.loads(requests.get('https://api.mail.tm/domains').text)['hydra:member'][0]['domain']
            print(domain)
            email = ''.join((random.choice('ie72ign8dka772ign8dka7u8sjkn28r') for i in range(10))) + "@" + domain
            password = "A1234567890"

            account_data = json.loads(requests.post('https://api.mail.tm/accounts', json = {
                'address': email,
                'password': password
            }).text)
            
            token = json.loads(requests.post('https://api.mail.tm/token', json = {
                'address': email,
                'password': password
            }).text)
            token = token['token']
            
            headers = {'Authorization': 'Bearer {}'.format(token)}

            driver.get("https://uptimerobot.com/signUp")
            driver.find_element(by=By.XPATH, value="/html/body/section/div/div[2]/div[1]/form/div[1]/input").send_keys(email.split("@")[0]) # login
            driver.find_element(by=By.XPATH, value="/html/body/section/div/div[2]/div[1]/form/div[2]/input").send_keys(email) # email
            driver.find_element(by=By.XPATH, value="/html/body/section/div/div[2]/div[1]/form/div[3]/input").send_keys(password) # haslo

            
            # driver.find_element(by=By.XPATH, value="/html/body/section/div/div[2]/div[1]/form/div[4]/div[1]/a/span[1]").click() # 1click
            # time.sleep(3)            
            # def tryClick():
            #     try:
            #         print(2)
            #         driver.find_element(by=By.XPATH, value="/html/body/div[5]/ul/li[1]/div").click() # click2
            #     except:
            #         print("not clicked")
            #         tryClick()
            #         pass
            # tryClick()
            
            #Capcha bypasser
            worked = True
            if check_exists_by_xpath("/html/body/section/div/div[2]/div[1]/form/div[5]/div/div/div/iframe"):
                captcha_res = "CAPCHA_NOT_READY"
                while captcha_res == "CAPCHA_NOT_READY":
                    try:
                        captcha_key = requests.get("http://2captcha.com/in.php?key=c122d98653490a5b663c7d93d54d6401&method=userrecaptcha&googlekey=6LeE3BETAAAAABvShHY2njRVSmbU7e2bquL4tPfw&pageurl=https://uptimerobot.com/signUp")
                        captcha_key = captcha_key.text.split("|")[1]
                        print("captcha_key: " + captcha_key)
                        time.sleep(15)
                        captcha_res = "CAPCHA_NOT_READY"
                        while captcha_res == "CAPCHA_NOT_READY":
                            captcha_res = requests.get("http://2captcha.com/res.php?key=c122d98653490a5b663c7d93d54d6401&action=get&id="+captcha_key).text
                            print(captcha_res)
                            if captcha_res == "CAPCHA_NOT_READY":
                                time.sleep(5)
                            else:
                                captcha_res = captcha_res.split("|")[1]
                        
                        # driver.execute_script("""function makeid(e){for(var t="",a="qwertyuiopasdfghjklzxcvbnm123".length,o=0;o<e;o++)t+="qwertyuiopasdfghjklzxcvbnm123".charAt(Math.floor(Math.random()*a));return t}email=makeid(19)+"@cldkid.com",username=makeid(14),console.log(email),console.log(username),e = '"""+captcha_res+"""',fetch("https://replit.com/signup",{credentials:"include",headers:{"User-Agent":"Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0",Accept:"application/json","Accept-Language":"en-US,en;q=0.5","content-type":"application/json","x-requested-with":"XMLHttpRequest","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin"},referrer:"https://replit.com/signup?from=landing",body:'{"email":"'+email+'","username":"'+username+'","password":"Ajndfifh783!","teacher":false,"organization":"","hCaptchaResponse":"'+e+'","hCaptchaSiteKey":"a20d9b66-6747-404a-9393-c449c4611661","source":"explicit"}',method:"POST",mode:"cors"});""")
                        time.sleep(10)
                        # driver.get('https://replit.com/~')
                    except Exception as e:
                        print(e)
                        pass
                driver.execute_script("a = document.getElementById('g-recaptcha-response'), a.style.display = 'visible', a.innerHTML = '"+captcha_res+"';")

            #Captcha done LOL
            time.sleep(2)
            driver.find_element(by=By.XPATH, value="/html/body/section/div/div[2]/div[1]/form/button").click()
            time.sleep(13)
            message_id = json.loads(requests.get('https://api.mail.tm/messages', headers=headers).text)
            message_id = message_id['hydra:member'][0]['id']
            message_data = json.loads(requests.get('https://api.mail.tm/messages/'+message_id, headers=headers).text)
            
            start = "here\n["
            end = "]."
            s = message_data['text']
            link = s[s.find(start)+len(start):s.rfind(end)]
            
            print(link)
            
            driver.get(link)
            driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div[3]/div[1]/ul/li[4]/a").click() # haslo
            time.sleep(6)
            driver.execute_script("window.scrollBy(0,2000);")
            time.sleep(2)
            driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div[3]/div[4]/div/div/div[5]/div/div[2]/div/div/fieldset/ul/li[1]/a").click() # haslo
            time.sleep(4)
            try:
                driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div[3]/div[4]/div/div/div[5]/div/div[2]/div/div/fieldset/ul/li[2]/div[1]/button").click()
                print("created new api key")
                time.sleep(10)
                
            except:
                print('api key alreade exist - reading')
                pass
            driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div[3]/div[4]/div/div/div[5]/div/div[2]/div/div/fieldset/ul/li[2]/div[2]/a").click() # haslo
            time.sleep(1)
            api_key = clipboard.paste()
            print(api_key)
            apikeys = json.load(open("../apikeys.json", "r"))
            apikeys[api_key] = 0
            with open("../apikeys.json", "w") as f:
                json.dump(apikeys, f, indent=2)
            # print(json.dumps(message_data, indent=4, sort_keys=True))
            
            driver.get("https://uptimerobot.com/inc/dml/userDML.php?action=logoutUser")
            # time.sleep(15)
            # changeProxy(driver)
        except Exception as e:
            print(e)
            

main()