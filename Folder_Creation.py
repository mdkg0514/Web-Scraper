import os
import pandas as pd
df = pd.read_csv("C:/Users/dwdqb/Desktop/Python Programs/Tires/Brands_name.csv")
# print(df.shape)
for i in range(1, 305):
    if (os.path.exists(f"C:/Users/dwdqb/Desktop/Python Programs/Tires/Data/{(df['Brands'][i]).capitalize()}")):
        continue
    else:
        os.mkdir(f"C:/Users/dwdqb/Desktop/Python Programs/Tires/Data/{(df['Brands'][i]).capitalize()}")
# import pandas as pd
# df = pd.read_csv("C:/Users/dwdqb/Desktop/Python Programs/SKLearn/movies.csv", index_col="Id")
# df['Title'] = df['Title'].shift(1)
# df.to_csv('C:/Users/dwdqb/Desktop/Python Programs/SKLearn/movies.csv')
# print(df.head())