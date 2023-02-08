from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from flask import Flask, render_template,request
from all_func_file import single_website,all_review_load,sen_analyzer

# chrome webdriver for running map 
driver=webdriver.Chrome(executable_path="C:\\Users\SKYNET\Downloads\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
url='https://www.google.com/maps/place'
driver.get(url)          
# wait for one website and then click review button
single_website(driver)
all_review_load(driver)
print(sen_analyzer(driver))

app=Flask(__name__,template_folder='./template')
@app.route("/")

def home():
  # search=driver.find_element(By.XPATH, "//*[@id='QA0Szd']/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]")
  # print(search)
  # return render_template('home.html')
  pass 
@app.route("/info",methods=["GET","POST"])
def info():
      # url='https://www.google.com/maps/place/kashful garden'
      # result=driver.get(url)
      # print(result)
      # return render_template('result.html',result=result)
      pass
if __name__=='__main__':
    app.run()