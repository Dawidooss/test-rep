DOMAIN = ".hckrteam.com"
X_AUTH_KEY = "9fdf3c82e2bd763823923c4bfe60e5ed24835"
X_AUTH_EMAIL = "gok.daw@wp.pl"
ZONE = "bd95700fc9ea1b27cc2fd19db9a89279"
APIKEY = "u1626722-7dd13e1bed6db0602d759dc8"
PINGER_TO_FORK = "https://replit.com/@Dawidooss/GrowlingJudiciousMoto-1?v=1"
BOT_TO_FORK = "https://replit.com/@tewyail11/Discord-BOt#main.sh"

class KontoIstnieje(Exception):
    pass
class Koniec(Exception):
    pass
class ZmienKonto(Exception):
    pass

from tabnanny import check

import undetected_chromedriver as uc

uc.install()

import http.client
import json
import os
import random
import subprocess
import time
import sys
from http.server import executable

import psutil
import pytest
import requests
import selenium
from colorama import Fore, Style
from selenium import webdriver
from selenium.common.exceptions import (NoSuchElementException,
                                        TimeoutException,
                                        UnexpectedAlertPresentException)
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#Main
os.system("cls")
os.system('title ' + 'Replit  ^| Account Generator ')
def logo():
    aio = Fore.CYAN +"""   
-------------- Replit Repl Generator ---------------
 _       _       _                                 
| |_  __| |___ _| |_ ___ __ _ _ __    __ ___ _ __  
| ' \/ _| / / '_|  _/ -_) _` | '  \ _/ _/ _ \ '  \ 
|_||_\__|_\_\_|  \__\___\__,_|_|_|_(_)__\___/_|_|_|
                                                   
--- fischٴ#9747 blue.z.czatu#9999 Dawidooss#2236 ---
                                                                                                                                                    
"""
    print(aio)
logo()

time.sleep(1)

from selenium.webdriver import Chrome
options = webdriver.ChromeOptions()
#PROXY = "45.192.145.218:5560" # IP:PORT or HOST:PORT
with open("proxy.txt") as f:
    lines = f.readlines()
PROXY = random.choice(lines)
#options.add_argument('--proxy-server="185.126.65.71:6856"')
options.add_argument('--proxy-server=%s' % PROXY)
driver = Chrome(options=options)
driver.set_window_size(1920, 1080)
conn = http.client.HTTPSConnection("api.uptimerobot.com")

def check_exists_by_xpath(xpath):
    try:
        driver.find_element(by=By.XPATH, value=xpath)
    except NoSuchElementException:
        return False
    return True

driver.set_script_timeout(99999999)

print("PID: " + str(os.getpid()))

def get_apikey():
    apikeys = json.load(open("../apikeys.json", "r"))
    for apikey, amount in apikeys.items():
        if amount > 40:
            continue
        inwork = json.load(open("apikeys_inwork.json", "r"))
        if apikey in inwork:
            try:
                psutil.Process(inwork[apikey])
                continue
            except:
                #PID is not running, you can use that
                pass
                
        pid = os.getpid()
        inwork[apikey] = pid
        json.dump(inwork, open("apikeys_inwork.json", "w"), indent=2)
        return {'apikey':apikey, 'amount': amount}
    return "NO_AVAIBLE"

# api key
os.system('title ' + 'Replit  ^| Account Generator')

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
} 

driver.get("https://replit.com/")

while True:

    pinger = ""

    work = True
    replit_bots = 0
    logged = False
    while not logged:
        time.sleep(3)
        try:
            #print(3)
            time.sleep(7)
            driver.get("https://replit.com/")
            captcha_key = requests.get("https://2captcha.com/in.php?key=40e599bbc44d7ecce11525027fb28f83&method=hcaptcha&invisible=1&proxy=abjthxoc:9kluj4f87mxp@"+PROXY+"&proxytype=HTTP&sitekey=a20d9b66-6747-404a-9393-c449c4611661&pageurl=repl.it")
            captcha_key = captcha_key.text.split("|")[1]
            print("Captcha Key: " + captcha_key)
            time.sleep(15)
            captcha_res = "CAPCHA_NOT_READY"
            while captcha_res == "CAPCHA_NOT_READY":
                captcha_res = requests.get("http://2captcha.com/res.php?key=40e599bbc44d7ecce11525027fb28f83&action=get&id="+captcha_key).text
                print(captcha_res)
                if captcha_res == "CAPCHA_NOT_READY":
                    time.sleep(5)
                else:
                    captcha_res = captcha_res.split("|")[1]
            driver.execute_script("""function makeid(e){for(var t="",a="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789",c=a.length,r=0;r<e;r++)t+=a.charAt(Math.floor(Math.random()*c));return t}let email=makeid(10),username=makeid(10),captcha='"""+captcha_res+"""';await fetch("https://replit.com/signup",{credentials:"include",headers:{"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0",Accept:"application/json","Accept-Language":"en-US,en;q=0.5","content-type":"application/json","x-requested-with":"XMLHttpRequest","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin"},referrer:"https://replit.com/signup?from=landing",body:'{"email":"'+email+'@rawr.com","username":"'+username+'","password":"sdjfhsehifjs!A1","teacher":false,"organization":"","hCaptchaResponse":"'+captcha+'","hCaptchaSiteKey":"a20d9b66-6747-404a-9393-c449c4611661","source":"explicit"}',method:"POST",mode:"cors"});""")
            time.sleep(10)
            print(captcha_res)
            print("Account Created")
            driver.get('https://replit.com/~')
            logged = True
        except Exception as e:
            print(e)
            pass
        time.sleep(5)
    worked = False
    failed = False
    while not worked:
        try:
            driver.get("https://replit.com/@Dawidooss/GrowlingJudiciousMoto?v=1")
            time.sleep(5)
            driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[3]/div/div/div[2]/div/button[1]").click()
            time.sleep(10)
            if check_exists_by_xpath("/html/body/div[5]/div/button"):
                driver.find_element(by=By.XPATH,value="/html/body/div[5]/div/button").click()
            if check_exists_by_xpath("/html/body/div[3]/div/div[1]/button"):
                driver.find_element(by=By.XPATH,value="/html/body/div[3]/div/div[1]/button").click()#V2
            time.sleep(15)
            driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[1]/header/div/div[2]/div/div[1]").click() #run
            time.sleep(50)

            random_url = ''.join((random.choice('ie72ign8dka772ign8dka7u8sjkn28r') for i in range(10)))

            time.sleep(1)
            driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[6]/div/div/div[2]/span/div/button").click()
            time.sleep(1)
            driver.find_element(by=By.XPATH, value="/html/body/reach-portal/div/div/div/div/ol/li/div/div/div/input").send_keys(random_url+DOMAIN)
            time.sleep(1)
            cname = driver.find_element(by=By.XPATH, value="/html/body/reach-portal/div/div/div/div/ol/li[2]/div/div[2]/div/div/input").get_attribute("value")

            print("CNAME: " + cname)

            cloudflare_headers = {
                'content-type': "application/json",
                'cache-control': "no-cache",
                "X-Auth-Email": X_AUTH_EMAIL,
                "X-Auth-Key": X_AUTH_KEY
            } 

            content = {
                "type": "CNAME",
                "name": "www."+random_url+DOMAIN,
                "content": random_url+DOMAIN,
                "ttl": 1
            }

            content2 = {
                "type": "CNAME",
                "name": random_url+DOMAIN,
                "content": cname,
                "ttl": 1
            }
            
            response = requests.request(
                "POST", 
                "https://api.cloudflare.com/client/v4/zones/"+ZONE+"/dns_records",
                headers=cloudflare_headers,
                json=content
            )
            print("Request to Cloudflare 1 sent!")
            time.sleep(5)
            response = requests.request(
                "POST", 
                "https://api.cloudflare.com/client/v4/zones/"+ZONE+"/dns_records",
                headers=cloudflare_headers,
                json=content2
            )
            time.sleep(5)
            driver.find_element(by=By.XPATH,value="/html/body/reach-portal/div/div/div/div/div[3]/div/button").click()
            time.sleep(1)
            driver.find_element(by=By.XPATH,value="/html/body/reach-portal/div/div/div/div/div[3]/div/button").click()
            time.sleep(10)
            #/html/body/reach-portal/div/div/div/div/div[3]/div/button

            url_i_name = "https://"+random_url+DOMAIN
            pinger = "https://"+random_url+DOMAIN

            payload = "api_key="+APIKEY+"&format=json&type=1&url="+url_i_name+"&friendly_name="+url_i_name
            url = "https://api.uptimerobot.com/v2/newMonitor"
            response = requests.request("POST", url, data=payload, headers=headers).text
            
            data = json.loads(response)
            stat = data['stat']
                        
            print("Status: " + stat)
            
            if stat == "ok":
                print("PINGER SUCCESS (https://"+random_url+DOMAIN+")")
                worked = True
            else:
                print("UpTimeRobot pełny! Wyłączanie")
                raise Koniec
        except Koniec:
            worked = True
            failed = True
        except Exception as e:
            print(e)
            pass
    if failed:
        sys.exit()
    driver.get("https://replit.com/logout")

    logged = False
    while not logged:
        time.sleep(3)
        try:
            #print(3)
            time.sleep(7)
            driver.get("https://replit.com/")
            captcha_key = requests.get("https://2captcha.com/in.php?key=40e599bbc44d7ecce11525027fb28f83&method=hcaptcha&invisible=1&proxy=abjthxoc:9kluj4f87mxp@"+PROXY+"&proxytype=HTTP&sitekey=a20d9b66-6747-404a-9393-c449c4611661&pageurl=repl.it")
            captcha_key = captcha_key.text.split("|")[1]
            print("Captcha Key: " + captcha_key)
            time.sleep(15)
            captcha_res = "CAPCHA_NOT_READY"
            while captcha_res == "CAPCHA_NOT_READY":
                captcha_res = requests.get("http://2captcha.com/res.php?key=40e599bbc44d7ecce11525027fb28f83&action=get&id="+captcha_key).text
                print(captcha_res)
                if captcha_res == "CAPCHA_NOT_READY":
                    time.sleep(5)
                else:
                    captcha_res = captcha_res.split("|")[1]
            driver.execute_script("""function makeid(e){for(var t="",a="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789",c=a.length,r=0;r<e;r++)t+=a.charAt(Math.floor(Math.random()*c));return t}let email=makeid(10),username=makeid(10),captcha='"""+captcha_res+"""';await fetch("https://replit.com/signup",{credentials:"include",headers:{"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0",Accept:"application/json","Accept-Language":"en-US,en;q=0.5","content-type":"application/json","x-requested-with":"XMLHttpRequest","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin"},referrer:"https://replit.com/signup?from=landing",body:'{"email":"'+email+'@rawr.com","username":"'+username+'","password":"sdjfhsehifjs!A1","teacher":false,"organization":"","hCaptchaResponse":"'+captcha+'","hCaptchaSiteKey":"a20d9b66-6747-404a-9393-c449c4611661","source":"explicit"}',method:"POST",mode:"cors"});""")
            time.sleep(10)
            print(captcha_res)
            print("Account Created")
            driver.get('https://replit.com/~')
            logged = True
        except Exception as e:
            print(e)
            pass
        time.sleep(5)

    while replit_bots < 500 and work:
        #print(4)
        time.sleep(3)
        try:
            driver.get("https://replit.com/~")
            if check_exists_by_xpath("/html/body/reach-portal/div[3]/div/div/div/div[2]/button"):
                driver.find_element(by=By.XPATH,value="/html/body/reach-portal/div[3]/div/div/div/div[2]/button").click()
            time.sleep(2)
            driver.get("https://replit.com/@PHPDeveloper01/Discord-BOt?v=1") #to fork
            time.sleep(3)
            if check_exists_by_xpath("/html/body/div[3]/div/div[1]/button"):
                driver.find_element(by=By.XPATH,value="/html/body/div[3]/div/div[1]/button").click()

            driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[3]/div/div/div[2]/div/button[1]").click() #fork
            print("Repl Forked 1/5")
            time.sleep(1)
            ########################
            time.sleep(10)
            if check_exists_by_xpath("/html/body/div[5]/div/button"):
                driver.find_element(by=By.XPATH,value="/html/body/div[5]/div/button").click()
            if check_exists_by_xpath("/html/body/div[3]/div/div[1]/button"):
                driver.find_element(by=By.XPATH,value="/html/body/div[3]/div/div[1]/button").click()#V2
            print("Skiped Tutorial 2/5")
            time.sleep(1)
            driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[1]/header/div/div[2]/div/div[1]").click() #run
            print("Clicked Run 3/5")
            time.sleep(10)
            print("Waiting: 10s")
            time.sleep(10)
            print("Waiting: 20s")
            time.sleep(10)
            print("Waiting: 30s")
            time.sleep(10)
            print("Waiting: 40s")
            time.sleep(10)
            print("Waiting: 50s")
            print("Success Replit 4/5")

            namerepl = driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[6]/div/div/input").get_attribute("value")

            requests.post(pinger, json=[namerepl])
            
            replit_bots += 1 
            print("Botow na replit: " + str(replit_bots))
        except Exception as e:
            print(e)
            pass
    time.sleep(5)
    logged = False
    driver.get("https://replit.com/logout")
    print("Replit Logout")
        
input()
