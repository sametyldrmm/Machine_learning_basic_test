import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import save_model, load_model
from sklearn.preprocessing import MinMaxScaler
import numpy as np
# CSV dosyasını okuma
data = pd.read_csv('veriler3.csv')

# değiştirelecekler
# Type_of_Loan "And " ların tamamı silinecek
# Payment_Behaviour değiştir
# !@9#%8
# Amount_invested_monthly
# 0 lar o grubun ortalaması ile değiştir // gerek kalmadı
# Monthly_Balance
# boş satırlar o grubun ortalamsı ile doldurulacak



############ Payment_Behaviour düzeltilecek ############
column = "Type_of_Loan"
# print(data[column])
data[column] = data[column].apply(lambda x: x.replace('and ', ''))
# print(data[column])
############ bitti ############

############ Payment_Behaviour düzeltilecek ############
column = "Payment_Behaviour"

customer_id = "CUS_0x7029"
# Belirli Customer_ID'ye bağlı değerleri filtreleyin
filtered_data = data[data['Customer_ID'] == customer_id]
# print(filtered_data['Payment_Behaviour'])

data[column] = data[column].replace('!@9#%8', method='ffill')
data[column] = data[column].replace('!@9#%8', method='bfill')

filtered_data = data[data['Customer_ID'] == customer_id]
# print(filtered_data['Payment_Behaviour'])
########### bitti ############
data['Monthly_Balance'] = data.groupby('Customer_ID')['Monthly_Balance'].fillna(method='ffill')
data['Monthly_Balance'] = data.groupby('Customer_ID')['Monthly_Balance'].fillna(method='bfill')

print(data["Monthly_Balance"].isnull().any())

print(data.dtypes)


##############3 data_controller #######################3


def controller(isimler):
  for i in isimler:
    print(data[i].isnull().any())


print(data["Age"].isnull().any())
veri = [
"Customer_ID",
"Month",
"Age",
"Occupation",
"Annual_Income",
"Monthly_Inhand_Salary",
"Num_Bank_Accounts",
"Num_Credit_Card",
"Interest_Rate",
"Num_of_Loan",
"Type_of_Loan",
"Delay_from_due_date",
"Num_of_Delayed_Payment",
"Changed_Credit_Limit",
"Num_Credit_Inquiries",
"Credit_Mix",
"Outstanding_Debt",
"Credit_Utilization_Ratio",
"Credit_History_Age",
"Payment_of_Min_Amount",
"Total_EMI_per_month",
"Amount_invested_monthly",
"Payment_Behaviour",
"Monthly_Balance",
"Credit_Score",
]



data['Credit_Score'] = data.groupby('Customer_ID')['Credit_Score'].fillna(method='ffill')
data['Credit_Score'] = data.groupby('Customer_ID')['Credit_Score'].fillna(method='bfill')

data['Payment_of_Min_Amount'] = data.groupby('Customer_ID')['Payment_of_Min_Amount'].fillna(method='ffill')
data['Payment_of_Min_Amount'] = data.groupby('Customer_ID')['Payment_of_Min_Amount'].fillna(method='bfill')
controller(veri)

data.to_csv("common.csv",index=False)




# Tam olarak bitmemiş bir aşama olsa da bir sonraki aşamaya geçiyorum