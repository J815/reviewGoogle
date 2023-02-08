# from flask1 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

import re
import nltk
nltk.downloader.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer
from flask import Flask, render_template,request

def single_website(driver):
    try:
     page_wait=WebDriverWait(driver,600).until(lambda x:x.find_element(By.XPATH,'//div[@role="button"]'))
     time.sleep(5)
     page_wait.click()
    except:
      quit

def all_review_load(driver):
 def counter_ele(driver,page):
  num=''
  try:
     s= driver.find_element(By.XPATH,'//div[@class="fontBodySmall"]')
     for i in s.text:
        if i.isdigit():
             num+=i
        else:
             break
     print(num)
  except:
     pass
  return num 
 def curr_counter(driver,page):
     size=page.size
     h=size['height']
     w=size['width']  
     time.sleep(3)
     action=ActionChains(driver)
     while True:
       action.move_to_element_with_offset(page,w*0.99,h*0.99).click().perform()
       action.send_keys(Keys.ARROW_DOWN).perform()
       time.sleep(3)
       try:
        if len(driver.find_elements(By.XPATH,'//div[@class="jftiEf fontBodyMedium"]'))==int(counter_ele(driver,page)):
                  return True
       except:
                  pass 
 try:
  load_wait=WebDriverWait(driver,400).until(lambda x: curr_counter(x,x.find_element(By.XPATH,'//div[@class="m6QErb DxyBCb kA9KIf dS8AEf"]')))
 except:
     pass          

def dic_all_elements(driver):
  dic_location={}
  x=1
  try:
    # make dictionary of all elements 
    for i in driver.find_elements(By.XPATH,'//div[@class="jftiEf fontBodyMedium"]'):   
     try:
         driver.find_element(By.XPATH,'//button[@class="w8nwRe kyuRq"]').click()
     except:
        pass
     try:
         review_date=i.find_element(By.XPATH,'.//span[@class="rsqaWe"]').text
         review_text=i.find_element(By.XPATH,'.//span[@class="wiI7pd"]').text.partition("\n\n")[0]
         review_rating=i.find_element(By.XPATH,'.//span[@class="kvMYJc"]').get_attribute('aria-label')
         dic_location[x]=(review_date,review_rating,review_text)
         x+=1
     except:
        pass
  except:
    pass
  return dic_location

def sen_analyzer(driver):
#   sentiment analysis for all reviews
  dic_location=dic_all_elements(driver)
  res_of_ana={}
  length_dic=len(dic_location)
  senia=SentimentIntensityAnalyzer()
  if length_dic>0:
    for k,v in dic_location.items():
     if v[2]:
       pola=senia.polarity_scores(v[2])
       if pola['compound']>=0.05:
        res='positive'
       elif pola['compound']<=-0.05:
        res='negative'
       else:
        res='neutral'
     else:
       res=None
     res_of_ana[k]=(v[0],v[1],res)
  return res_of_ana
       