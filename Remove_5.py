import pandas as pd
import time
df = pd.read_csv("C:/Users/dwdqb/Desktop/Python Programs/Tires/Brands_name.csv")
for i in range(len(df)):
    path = f"C:/Users/dwdqb/Desktop/Python Programs/Tires/Data/{(df['Brands'][i]).capitalize()}/Refined_links.csv"
    try:
        df2 = pd.read_csv(path)
        df2.drop([0, 1, 2, 3, 4, 5], axis=0, inplace=True)
        df2.dropna()
        print(df2.head(2))
        df2.to_csv(path, index=False)
        # time.sleep(5)
    except:
        continue