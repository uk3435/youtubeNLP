import time
from selenium import webdriver
from selenium.webdriver import Chrome 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from langdetect import detect
data=[]



options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : 'C:/Users/Desktop'}
options.add_experimental_option('prefs', prefs)
options.add_argument("window-size=1200x600")
options.add_experimental_option('useAutomationExtension', False)


with Chrome(executable_path=r'C:\Users\Desktop\youtubeNLP\chromedriver.exe',chrome_options=options) as driver:

    
    wait = WebDriverWait(driver,15)
    driver.get("https://www.youtube.com/watch?v=*****") # video url


    for item in range(4): 
       
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.PAGE_DOWN)
             
        time.sleep(15)

    for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content"))):
        data.append(comment.text)




f = open("y1.txt", "a", encoding="utf-8")



for i in range(len(data)):
    
    f.write(data[i])
    f.close()

