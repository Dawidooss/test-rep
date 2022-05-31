while True:
    try:
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
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
        import subprocess
        import time
        import requests
        import pytest
        import time
        import json
        import random



        #Main
        os.system("cls")
        os.system('title ' + 'Interia  ^| Account Generator ')
        def logo():
            aio = Fore.CYAN +"""   
                                
    ╔════════════════════╗    ___           _                   _         
    |  fisch#5816        |   |_ _|  _ __   | |_    ___   _ __  (_)   __ _ 
    |  blue.z.czatu#9999 |    | |  | '_ \  | __|  / _ \ | '__| | |  / _` |
    |  v1.2              |    | |  | | | | | |_  |  __/ | |    | | | (_| |
    ╚════════════════════╝   |___| |_| |_|  \__|  \___| |_|    |_|  \__,_|

                                                                                                                                                            
        """
            print(aio)
        logo()

        time.sleep(1)




        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"     
        options = webdriver.ChromeOptions()
        options.headless = False
        options.add_argument(f'user-agent={user_agent}')
        options.add_argument("--window-size=1920,1080")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-running-insecure-content')
        options.add_argument("--disable-extensions")
        options.add_argument("--proxy-server='direct://'")
        options.add_argument("--proxy-bypass-list=*")
        options.add_argument('--disable-gpu') 
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        options.add_argument("--mute-audio")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
        driver.set_window_size(800, 1000)
        driver.get("https://konto-pocztowe.interia.pl/#/nowe-konto/darmowe")
        os.system("cls")
        logo()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[3]/div[2]/button[3]").click()                                
        time.sleep(1)
        result_str = ''.join((random.choice('PolakCebulak3sG33aXD') for i in range(10)))
        password = ''.join((random.choice('amvie72ign8dka7u8sjkn28r') for i in range(25)))+"A!"
        name = ''.join((random.choice('ie72ign8dka772ign8dka7u8sjkn28r') for i in range(10)))
        #config
        emailname = "x"+name+"earn"#<emailname>@<hubname>hub.pl
        hubname = "ice"#<emailname>@<hubname>hub.pl
        redirectemail = "dawid.pro123@interia.pl"#sending all messages from generated accounts to this email (only interia email)
        #Account main-alt
        os.system("cls")
        logo()
        time.sleep(1.5)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div/form/div[1]/div[1]/input").send_keys(emailname)
        time.sleep(0.5)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div/form/div[1]/div[2]/input").send_keys("mai")
        time.sleep(0.5)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div/form/div[1]/div[3]/div[1]/input").send_keys("5")
        time.sleep(0.1)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div/form/div[1]/div[3]/div[2]/div[1]").click()  
        time.sleep(0.1)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div/form/div[1]/div[3]/div[2]/ul/li[5]").click()  
        time.sleep(0.1)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div/form/div[1]/div[3]/div[3]/input").send_keys("1999")
        time.sleep(0.1)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div/form/div[1]/div[6]/div/input").send_keys(password)
        time.sleep(0.1)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div/form/div[1]/div[7]/div/input").send_keys(password)
        time.sleep(0.1)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div/form/div[1]/div[4]/div[1]").click()  
        time.sleep(0.1)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div/form/div[1]/div[4]/ul/li[1]/span[2]").click()  
        time.sleep(0.1)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div/form/div[1]/div[5]/div[1]/input").send_keys("n")
        time.sleep(0.1)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div/form/div[2]/div[1]/div[1]/label").click()  
        time.sleep(0.1)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div/form/div[2]/button").click()  
        time.sleep(5)
        driver.get("https://poczta.interia.pl/next/")
        os.system("cls")
        logo()
        print(f'    Email Genereted:'+emailname+'.main@interia.pl')
        #account 1
        time.sleep(0.5)
        driver.get("https://ustawienia.interia.pl/poczta/konta-zewnetrzne/dodaj-alias?")
        time.sleep(0.1)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/form/table/tbody/tr[1]/td[2]/input").send_keys(emailname+"1")#<emailname>@<hubname>hub.pl
        time.sleep(0.1)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/form/table/tbody/tr[1]/td[2]/div[1]/div[2]/div[1]/span").click()#click select
        time.sleep(0.1)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/form/table/tbody/tr[1]/td[2]/div[1]/div[2]/div[2]/div/div[13]").click()#select hub
        time.sleep(0.1)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/form/table/tbody/tr[1]/td[2]/span[2]/input").send_keys(hubname)#<emailname>@<hubname>hub.pl
        time.sleep(0.1)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/form/label").click()#box email
        time.sleep(0.5)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/form/div[2]/input").click()#create alias
        time.sleep(0.5)
        print(f'    Email Genereted:'+emailname+'1@'+hubname+'.hub.pl')
        #account 2
        time.sleep(0.5)
        driver.get("https://ustawienia.interia.pl/poczta/konta-zewnetrzne/dodaj-alias?")
        time.sleep(0.1)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/form/table/tbody/tr[1]/td[2]/input").send_keys(emailname+"2")#<emailname>@<hubname>hub.pl
        time.sleep(0.1)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/form/table/tbody/tr[1]/td[2]/div[1]/div[2]/div[1]/span").click()#click select
        time.sleep(0.1)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/form/table/tbody/tr[1]/td[2]/div[1]/div[2]/div[2]/div/div[13]").click()#select hub
        time.sleep(0.1)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/form/table/tbody/tr[1]/td[2]/span[2]/input").send_keys(hubname)#<emailname>@<hubname>hub.pl
        time.sleep(0.1)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/form/label").click()#box email
        time.sleep(0.5)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/form/div[2]/input").click()#create alias
        time.sleep(0.5)
        print(f'    Email Genereted:'+emailname+'2@'+hubname+'.hub.pl')
        #account 3
        time.sleep(0.5)
        driver.get("https://ustawienia.interia.pl/poczta/konta-zewnetrzne/dodaj-alias?")
        time.sleep(0.1)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/form/table/tbody/tr[1]/td[2]/input").send_keys(emailname+"3")#<emailname>@<hubname>hub.pl
        time.sleep(0.1)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/form/table/tbody/tr[1]/td[2]/div[1]/div[2]/div[1]/span").click()#click select
        time.sleep(0.1)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/form/table/tbody/tr[1]/td[2]/div[1]/div[2]/div[2]/div/div[13]").click()#select hub
        time.sleep(0.1)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/form/table/tbody/tr[1]/td[2]/span[2]/input").send_keys(hubname)#<emailname>@<hubname>hub.pl
        time.sleep(0.1)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/form/label").click()#box email
        time.sleep(0.5)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/form/div[2]/input").click()#create alias
        time.sleep(0.5)
        print(f'    Email Genereted:'+emailname+'3@'+hubname+'.hub.pl')
        #account 4
        time.sleep(0.5)
        driver.get("https://ustawienia.interia.pl/poczta/konta-zewnetrzne/dodaj-alias?")
        time.sleep(0.1)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/form/table/tbody/tr[1]/td[2]/input").send_keys(emailname+"4")#<emailname>@<hubname>hub.pl
        time.sleep(0.1)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/form/table/tbody/tr[1]/td[2]/div[1]/div[2]/div[1]/span").click()#click select
        time.sleep(0.1)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/form/table/tbody/tr[1]/td[2]/div[1]/div[2]/div[2]/div/div[13]").click()#select hub
        time.sleep(0.1)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/form/table/tbody/tr[1]/td[2]/span[2]/input").send_keys(hubname)#<emailname>@<hubname>hub.pl
        time.sleep(0.1)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/form/label").click()#box email
        time.sleep(0.5)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/form/div[2]/input").click()#create alias
        time.sleep(0.5)
        print(f'    Email Genereted:'+emailname+'4@'+hubname+'.hub.pl')
        #account 5
        time.sleep(0.5)
        driver.get("https://ustawienia.interia.pl/poczta/konta-zewnetrzne/dodaj-alias?")
        time.sleep(0.1)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/form/table/tbody/tr[1]/td[2]/input").send_keys(emailname+"5")#<emailname>@<hubname>hub.pl
        time.sleep(0.1)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/form/table/tbody/tr[1]/td[2]/div[1]/div[2]/div[1]/span").click()#click select
        time.sleep(0.1)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/form/table/tbody/tr[1]/td[2]/div[1]/div[2]/div[2]/div/div[13]").click()#select hub
        time.sleep(0.1)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/form/table/tbody/tr[1]/td[2]/span[2]/input").send_keys(hubname)#<emailname>@<hubname>hub.pl
        time.sleep(0.1)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/form/label").click()#box email
        time.sleep(0.5)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/form/div[2]/input").click()#create alias
        time.sleep(0.5)
        print(f'    Email Genereted:'+emailname+'5@'+hubname+'.hub.pl')
        #redirect email
        driver.get("https://ustawienia.interia.pl/poczta/ustawienia")
        time.sleep(0.5)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/form/table/tbody/tr[11]/td[1]/input").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/form/table/tbody/tr[11]/td[1]/input").send_keys(redirectemail)
        time.sleep(0.5)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/form/div/input").click()
        time.sleep(0.5)
        #save data
        print(f'    Emails Saved in email.txt and email-password.txt')
        with open('log.txt', 'a') as f:
            f.write(emailname+"1@"+hubname+".hub.pl\n")
            f.write(emailname+"2@"+hubname+".hub.pl\n")
            f.write(emailname+"3@"+hubname+".hub.pl\n")
            f.write(emailname+"4@"+hubname+".hub.pl\n")
            f.write(emailname+"5@"+hubname+".hub.pl\n")
        with open('logg.txt', 'a') as f:
            f.write(emailname+"1@"+hubname+".hub.pl:"+password+"\n")
            f.write(emailname+"2@"+hubname+".hub.pl:"+password+"\n")
            f.write(emailname+"3@"+hubname+".hub.pl:"+password+"\n")
            f.write(emailname+"4@"+hubname+".hub.pl:"+password+"\n")
            f.write(emailname+"5@"+hubname+".hub.pl:"+password+"\n")
            time.sleep(15)
            driver.close()
            
        time.sleep(3)
    except:
        driver.close()
        print(f'    ERROR')
        pass