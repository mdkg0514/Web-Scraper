from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
driver = webdriver.Chrome()
df = pd.read_csv("C:/Users/dwdqb/Desktop/Python Programs/Tires/Brands_name.csv")
df.drop_duplicates(inplace=True)
wait = WebDriverWait(driver,10)
for i in range(len(df)):
    types = []
    refined_types = []
    link_list = []
    base_url = f"https://simpletire.com/brands/{df['Brands'][i]}"
    name = df['Brands'][i].strip("tires")
    driver.get(base_url)
    wait = WebDriverWait(driver,10)
    driver.execute_script("window.scrollBy(0, 1500);")
    try:
        menu = wait.until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[2]/div/div[2]/main/div/div/div[7]/div/div[2]/div/div[2]/div/div[1]/div/div/div/div/ul/li[6]/a")))
        menu.click()
        time.sleep(3)
        links = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "itemButton ")))
        for link in links:
            new_link = link.get_attribute("href")
            print(new_link)
            link_list.append(new_link)
        df2 = pd.DataFrame({"Links":link_list})
        df2.to_csv(f"C:/Users/dwdqb/Desktop/Python Programs/Tires/Data/{df['Brands'][i].capitalize()}/Refined_links.csv")
    except:
        try:
            link = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "css-1rka3yc")))
            link.click()
            time.sleep(3)
            links = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "itemButton ")))
            for link in links:
                new_link = link.get_attribute("href")
                print(new_link)
                link_list.append(new_link)
            df2 = pd.DataFrame({"Links":link_list})
            df2.to_csv(f"C:/Users/dwdqb/Desktop/Python Programs/Tires/Data/{df['Brands'][i].capitalize()}/Refined_links.csv")
        except Exception as e:
            # print(f"The error is {e}")
            continue