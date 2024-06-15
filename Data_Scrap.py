from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import pandas as pd
user_data_dir = "C:/Users/dwdqb/AppData/Local/Google/Chrome"
profile_dir = "Dawood"

options = Options()
options.add_argument(f"--user-data-dir={user_data_dir}")
options.add_argument(f"--profile-directory={profile_dir}")
driver = webdriver.Chrome(options=options)
path = f"C:/Users/dwdqb/Desktop/Python Programs/Tires/Data/Continental-tires/Refined_links.csv"
data = pd.read_csv(path)

driver.get("https://simpletire.com/brands/continental-tires/4x4-sportcontact")
wait = WebDriverWait(driver,20)
base_col = ["Name", "Price", "Review", "Life", "Handling", "Traction"]
columns_n = []
column_class = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "css-1ojsquv")))
for column in column_class:
    columns_n.append(column.text)
columns_n.append("Sizes")
base_col.extend(columns_n)
count = 0
for i in base_col:
    count = count + 1
print(count)
df2 = pd.read_csv("C:/Users/dwdqb/Desktop/Python Programs/Tires/Brands_name.csv")


# for i in range(1):
for i in range(6, len(df2)):
    path = f"C:/Users/dwdqb/Desktop/Python Programs/Tires/Data/{(df2['Brands'][i]).capitalize()}/Refined_links.csv"
    if os.path.exists(path):
        data = pd.read_csv(path)
        data.dropna(inplace=True)
        for indx in range(len(data)):
        # for indx in range(1):
            driver.get(data["Links"][indx])
            # driver.get("https://simpletire.com/brands/accelera-tires/gamma")
            time.sleep(7)
            rows = []
            try:
                row_data = []
                columns_ = ["Name", "Price", "Review", "Life", "Handling", "Traction"]
                adt = ["NA" for l in range(len(base_col))]
                title = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'css-1wkv4b1'))).text
                print(title)
                price = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "css-1wdv3rw"))).text
                print(price)
                driver.execute_script("window.scrollBy(0, 500);")
                review = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'css-1opkmdm'))).text
                print(review)
                time.sleep(2)
                life = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="productDetailContainer"]/div[1]/div[2]/div/div[5]/div/ul/li[1]/div/div[3]/div/div[1]/div/div/h2'))).text
                print(life)
                handling = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="productDetailContainer"]/div[1]/div[2]/div/div[5]/div/ul/li[1]/div/div[3]/div/div[2]/div/div/h2'))).text
                print(handling)
                traction = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="productDetailContainer"]/div[1]/div[2]/div/div[5]/div/ul/li[1]/div/div[3]/div/div[3]/div/div/h2'))).text
                print(traction)
                row_data.append(title)
                row_data.append(price)
                row_data.append(review)
                row_data.append(life)
                row_data.append(handling)
                row_data.append(traction)
                print("Move down successfully")
                driver.execute_script("window.scrollBy(0, 3000);")
                column_class = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "css-1ojsquv")))
                for column in column_class:
                    columns_.append(column.text)
                columns_.append("Sizes")
                # driver.execute_script("window.scrollBy(0, 1000);")
                elements_class_1 = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "css-1up9wr3")))
                for element in elements_class_1:
                    row_data.append(element.text)
                    print(element.text)
                elements_class = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "css-1eo6wyy")))
                for element in elements_class:
                    row_data.append(element.text)
                    print(element.text)
                size_tab = wait.until(EC.element_to_be_clickable((By.ID,"tab-button-SiteProductSpecs-1")))
                size_tab.click()
                time.sleep(3)
                sizes = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "css-2ndw39")))
                size_text = [' '.join(sizes[0].text)]
                print(size_text)
                row_data.append(size_text)
                for i in columns_:
                    if i in base_col:
                        idx = base_col.index(i)
                        adt[idx] = row_data[columns_.index(i)]
                    else:
                        continue
                         
                print(base_col)
                print(adt)
                rows.append(adt)
            except:
                continue
        df = pd.DataFrame(rows, columns=base_col)
        df.to_csv(f"C:/Users/dwdqb/Desktop/Python Programs/Tires/Data/{(df2['Brands'][i]).capitalize()}/Data.csv")
        print("File created successfully.")
    else:
        continue