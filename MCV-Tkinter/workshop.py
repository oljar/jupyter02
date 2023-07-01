import pandas as pd
import csv

x_tag = 'M51: Pa'
y_tag = 'M53: Pa'
name = 'data_3.csv'




data_list = []
with open(name,'r')as f:
    data = csv.reader(f)
    for i in data:
        data_list.append(i)

result_row_number = []
for row_number , row  in enumerate(data_list):
    if str(x_tag) in str(row) :
        result_row_number.append(row_number)


print (int(result_row_number[0]))
df1 = pd.read_csv(name,sep=';', decimal=',' , header =int(result_row_number[0]) )
print (df1)





# result = print(df1.eq(value).any(axis=1))



#df1 = pd.read_csv(name,sep=';', decimal=',' , header= 0)


#
# # Przykład użycia
# file_path = 'plik.csv'
# value = 'szukana wartość'
# row_number = find_row_number(file_path, value)
# print(f'Numer wiersza: {row_number}')