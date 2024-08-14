print("hello")
import pandas as pd

df = pd.ExcelFile('Location Sheet.xlsx')
print(df)
df1 = pd.read_excel(df, 'Sheet7')
print(df1)