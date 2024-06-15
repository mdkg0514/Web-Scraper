from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
driver = webdriver.Chrome()
brands = []
base_url = f"https://simpletire.com/brands"
driver.get(base_url)
df = pd.DataFrame()
response = driver.page_source
wait = WebDriverWait(driver,10)
for i in range (1, 7):
    time.sleep(2)
    element = wait.until(EC.presence_of_element_located((By.XPATH, f'/html/body/div[2]/div/div[2]/main/div/div[3]/div[3]/div[{i}]/div/a/div[2]'))).text
    element_text = element.lower() + '-tires'
    print(element_text)
    brands.append(element_text)
for i in range (1, 300):
    # driver.execute_script("window.scrollBy(0, 1000);")
    time.sleep(2)
    element = wait.until(EC.presence_of_element_located((By.XPATH, f'/html/body/div[2]/div/div[2]/main/div/div[3]/div[5]/div[{i}]/div/a/div[2]'))).text
    new_element = element.replace(" ", "-")
    element_text = new_element.lower() + '-tires'
    print(element_text)
    brands.append(element_text)
df['Brands'] = brands
df.to_csv("C:/Users/dwdqb/Desktop/Python Programs/Tires/Brands_name.csv")