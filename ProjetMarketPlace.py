#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 13:05:20 2021

@author: victorbuzy
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re

options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument('window-size=1200x600') # optional



Path = '/Users/victorbuzy/Desktop/projetpython/chromedriver'
driver = webdriver.Chrome(Path)

driver.get("https://www.facebook.com/marketplace/?ref=app_tab")
time.sleep(4)

search = driver.find_element_by_css_selector('body > div > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.pfnyh3mw.jifvfom9.gs1a9yip.owycx6da.btwxx1t3.buofh1pr.dp1hu0rb > div.rq0escxv.l9j0dhe7.tkr6xdv7.j83agx80.cbu4d94t.pfnyh3mw.d2edcug0.hpfvmrgz.dp1hu0rb.rek2kq2y.o36gj0jk.ahb00how > div > div.rq0escxv.l9j0dhe7.du4w35lb.n851cfcs.aahdfvyu > div > div > span > div > div > div > div > label > input')
search.send_keys('Table')
search.send_keys(Keys.RETURN)

time.sleep(4)

Price = driver.find_element_by_css_selector ('body>div > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.pfnyh3mw.jifvfom9.gs1a9yip.owycx6da.btwxx1t3.buofh1pr.dp1hu0rb > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.cbu4d94t.g5gj957u.d2edcug0.hpfvmrgz.rj1gh0hx.buofh1pr.dp1hu0rb > div > div > div.fome6x0j.tkqzz1yd.aodizinl.fjf4s8hc.f7vcsfb0 > div:nth-child(1)')
Price=Price.text
print(Price)


regex = re.findall('\$\d+',Price)
print(regex)
char = '$'
  
# Remove character from Strings list 
# using loop + replace() + enumerate() 
res = [ele.replace(char, '') for ele in regex]
print (res)
#res = [str(i) for i in res]
res = [int(value) for value in res]

def Moyenne(l):
    avg = sum(l) / len(l)
    return avg

moyenne = Moyenne(res)
print("The average is $ :", moyenne)
    

driver.close()
driver.quit()