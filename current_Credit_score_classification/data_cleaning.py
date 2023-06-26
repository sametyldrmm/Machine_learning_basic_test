import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import save_model, load_model
from sklearn.preprocessing import MinMaxScaler
import numpy as np
# CSV dosyasını okuma
data = pd.read_csv('train.csv', error_bad_lines=False)

# print( len(data['Customer_ID'].unique()))

####################### Burada tüm kullanılanıcıların aynı aylarda verisinin olup olmadığını inceleyeceğiz #####################
# Kullanıcı ID'si ve var olan ayların olduğu sütunları seçin
kullanici_sutunu = 'Customer_ID'
ay_sutunu = 'Month'
df = data[[kullanici_sutunu, ay_sutunu]].copy()

gruplanmis_df = df.groupby(kullanici_sutunu)[ay_sutunu].nunique().reset_index()

aylarin_sayisi = gruplanmis_df[ay_sutunu].nunique()

if aylarin_sayisi == 1:
    print("Tüm kullanıcıların aynı aylara sahip verisi bulunuyor.")
else:
    print("Kullanıcılar arasında farklı aylara sahip veri bulunuyor.")

# ############################ burada biter ################################




##################3 işimize yaramayacak verileri temizleyelim  ##################33
data = data.drop("SSN",axis=1)
data = data.drop("Name",axis=1)
############################ burada biter ################################


# ################### Age sütunumuzda bazı değişkenlerimiz problemliydi onu çözmeye çalıştık ###################
customer_id = "CUS_0x2dbc"
# Belirli Customer_ID'ye bağlı değerleri filtreleyin
filtered_data = data[data['Customer_ID'] == customer_id]
print(filtered_data["Age"])
# Boş Occupation değerlerini Customer_ID'ye göre en yaygın değerle doldurma
data['Age'] = data.groupby('Customer_ID')['Age'].transform(lambda x: x.mode().iat[0])
# Belirli Customer_ID'ye bağlı değerleri filtreleyin
filtered_data = data[data['Customer_ID'] == customer_id]
print(filtered_data["Age"])
# ############################ burada biter ################################

# ###################Occupation sütunumuzda bazı değişkenlerimiz problemliydi onu çözmeye çalıştık ###################
customer_id = "CUS_0x2dbc"
# Belirli Customer_ID'ye bağlı değerleri filtreleyin
filtered_data = data[data['Customer_ID'] == customer_id]
print(filtered_data["Occupation"])
# Boş Occupation değerlerini Customer_ID'ye göre en yaygın değerle doldurma
data['Occupation'] = data.groupby('Customer_ID')['Occupation'].transform(lambda x: x.mode().iat[0])
# Belirli Customer_ID'ye bağlı değerleri filtreleyin
filtered_data = data[data['Customer_ID'] == customer_id]
print(filtered_data["Occupation"])
# ############################ burada biter ################################


# ###################Annual_Income sütunumuzda bazı değişkenlerimiz problemliydi onu çözmeye çalıştık ###################
customer_id = "CUS_0x21b1"
# Belirli Customer_ID'ye bağlı değerleri filtreleyin
filtered_data = data[data['Customer_ID'] == customer_id]
print(filtered_data["Annual_Income"])
# Boş Occupation değerlerini Customer_ID'ye göre en yaygın değerle doldurma
data['Annual_Income'] = data.groupby('Customer_ID')['Annual_Income'].transform(lambda x: x.mode().iat[0])
# Belirli Customer_ID'ye bağlı değerleri filtreleyin
filtered_data = data[data['Customer_ID'] == customer_id]
print(filtered_data["Annual_Income"])
# ############################ burada biter ################################

# ###################Monthly_Inhand_Salary sütunumuzda bazı değişkenlerimiz problemliydi onu çözmeye çalıştık ###################
customer_id = "CUS_0x21b1"
# Belirli Customer_ID'ye bağlı değerleri filtreleyin
filtered_data = data[data['Customer_ID'] == customer_id]
print(filtered_data["Monthly_Inhand_Salary"])
# Boş Occupation değerlerini Customer_ID'ye göre en yaygın değerle doldurma
data['Monthly_Inhand_Salary'] = data.groupby('Customer_ID')['Monthly_Inhand_Salary'].transform(lambda x: x.mode().iat[0])
# Belirli Customer_ID'ye bağlı değerleri filtreleyin
filtered_data = data[data['Customer_ID'] == customer_id]
print(filtered_data["Monthly_Inhand_Salary"])
# ############################ burada biter ################################

# ###################Num_Bank_Accounts sütunumuzda bazı değişkenlerimiz problemliydi onu çözmeye çalıştık ###################
customer_id = "CUS_0x21b1"
# Belirli Customer_ID'ye bağlı değerleri filtreleyin
filtered_data = data[data['Customer_ID'] == customer_id]
print(filtered_data["Num_Bank_Accounts"])
# Boş Occupation değerlerini Customer_ID'ye göre en yaygın değerle doldurma
data['Num_Bank_Accounts'] = data.groupby('Customer_ID')['Num_Bank_Accounts'].transform(lambda x: x.mode().iat[0])
# Belirli Customer_ID'ye bağlı değerleri filtreleyin
filtered_data = data[data['Customer_ID'] == customer_id]
print(filtered_data["Num_Bank_Accounts"])
# ############################ burada biter ################################


# ###################Num_Credit_Card sütunumuzda bazı değişkenlerimiz problemliydi onu çözmeye çalıştık ###################
customer_id = "CUS_0x21b1"
# Belirli Customer_ID'ye bağlı değerleri filtreleyin
filtered_data = data[data['Customer_ID'] == customer_id]
print(filtered_data["Num_Credit_Card"])
# Boş Occupation değerlerini Customer_ID'ye göre en yaygın değerle doldurma
data['Num_Credit_Card'] = data.groupby('Customer_ID')['Num_Credit_Card'].transform(lambda x: x.mode().iat[0])
# Belirli Customer_ID'ye bağl    ı değerleri filtreleyin
filtered_data = data[data['Customer_ID'] == customer_id]
print(filtered_data["Num_Credit_Card"])
# ############################ burada biter ################################

# ###################Interest_Rate sütunumuzda bazı değişkenlerimiz problemliydi onu çözmeye çalıştık ###################
customer_id = "CUS_0x21b1"
# Belirli Customer_ID'ye bağlı değerleri filtreleyin
filtered_data = data[data['Customer_ID'] == customer_id]
print(filtered_data["Interest_Rate"])
# Boş Occupation değerlerini Customer_ID'ye göre en yaygın değerle doldurma
data['Interest_Rate'] = data.groupby('Customer_ID')['Interest_Rate'].transform(lambda x: x.mode().iat[0])
# Belirli Customer_ID'ye bağlı değerleri filtreleyin
filtered_data = data[data['Customer_ID'] == customer_id]
print(filtered_data["Interest_Rate"])
# ############################ burada biter ################################

# ###################Num_of_Loan sütunumuzda bazı değişkenlerimiz problemliydi onu çözmeye çalıştık ###################
# burada num_of_loan değerleri type_of_loana göre düzenlencek type_of_loan leni kullanılabilir
customer_id = "CUS_0x21b1"
# Belirli Customer_ID'ye bağlı değerleri filtreleyin
filtered_data = data[data['Customer_ID'] == customer_id]
print(filtered_data["Num_of_Loan"])
# Boş Occupation değerlerini Customer_ID'ye göre en yaygın değerle doldurma
data['Num_of_Loan'] = data.groupby('Customer_ID')['Num_of_Loan'].transform(lambda x: x.mode().iat[0])
# Belirli Customer_ID'ye bağlı değerleri filtreleyin
filtered_data = data[data['Customer_ID'] == customer_id]
print(filtered_data["Num_of_Loan"])
# ############################ burada biter ################################


# ###################Type_of_Loan.. sütunumuzda bazı değişkenlerimiz problemliydi onu çözmeye çalıştık ###################
customer_id = "CUS_0x21b1"
# Belirli Customer_ID'ye bağlı değerleri filtreleyin
# Boş değerleri doldurmak istediğiniz sütunun adını belirtin
loan_sutunu = 'Type_of_Loan'

# Boş değerleri tespit edin
bos_degerler = data[data[loan_sutunu].isnull()]
print(bos_degerler)
data[loan_sutunu].fillna("Not Specified", inplace=True)
bos_degerler = data[data[loan_sutunu].isnull()]
print(bos_degerler)

# verimizde , ile ayrılmış bazı ifadeler vardı bunları çıkardık
data['Type_of_Loan'] = data['Type_of_Loan'].str.split(',')

# bu yeni verilerde var olan "and " ifadesini çıkarıyoruz
data['Type_of_Loan'] = data['Type_of_Loan'].apply(lambda x: [item.strip() for item in x if item.strip() != 'and '])

############# burası veriler temizlendikten sonra 2.aşama olarak verilerbilir benzer işlemleri çokça kullanıcaz
  # # One-Hot Encoding işlemi
  # one_hot_encoded_data = pd.get_dummies(data['Type_of_Loan'].apply(pd.Series).stack()).sum(level=0)

  # # One-Hot Encoding sonuçlarını veri setine ekleme
  # data = pd.concat([data, one_hot_encoded_data], axis=1)
############
# ############################ burada biter ################################


# ################### Delay_from_due_date sütunumuzda bir problem varmı bunu anlamaya çalışıcaz ###################
is_null = data['Delay_from_due_date'].isnull().any()

# Null değer varsa True, yoksa False döner
print(is_null)

non_integer_values = data['Delay_from_due_date'][~data['Delay_from_due_date'].apply(lambda x: str(x).lstrip('-').replace('.', '').isdigit())]

# Non-integer ifadeleri içeren satırları yazdırmak
print(len(non_integer_values) == 0)
# çıktılarımıza bakar isek bir sıkıntı yok gibi
# ############################ burada biter ################################



# ###################Num_of_Delayed_Payment sütunumuzda bazı değişkenlerimiz problemliydi onu çözmeye çalıştık ###################
# burada Num_of_Delayed_Payment değerleri Delay_from_due_date göre düzenlencek
# şöyle bir ilerleme kaydediyoruz ilk başta boş satırları en çok kullanılan ile dolduruyoruz
# "_" karakterini silme ve boş değerleri en çok kullanılan değerle doldurma fonksiyonu
customer_id = "CUS_0x5407"
# Belirli Customer_ID'ye bağlı değerleri filtreleyin
filtered_data = data[data['Customer_ID'] == customer_id]
print(filtered_data["Num_of_Delayed_Payment"])

def clean_and_fill(column):
    column = column.str.replace('_', '')
    most_common_value = column.mode().iat[0]
    column = column.fillna(most_common_value)
    return column.astype(int)

# Customer_ID'ye göre gruplandırma ve işlem uygulama
data['Num_of_Delayed_Payment'] = data.groupby('Customer_ID')['Num_of_Delayed_Payment'].transform(clean_and_fill)

customer_ids = data['Customer_ID'].unique()

# Her bir Customer_ID için Num_of_Delayed_Payment değerlerini güncelleme
data['Num_of_Delayed_Payment'] = data.groupby('Customer_ID')['Num_of_Delayed_Payment'].transform(lambda x: x.min())

# şimdi boş satılar dolduruldu ve diğer yazılar minumuma göre dolduruldu
# şimdi Delay_from_due_date e göre bu satırları artırıcaz eğer 30 günden az ise artırma gerçekleşmez fazla ise gerçekleşir
customer_ids = data['Customer_ID'].unique()

# Her bir Customer_ID için Num_of_Delayed_Payment değerlerini güncelleme

data['Num_of_Delayed_Payment'] += data.groupby('Customer_ID')['Delay_from_due_date'].transform(lambda x: (x > 30).cumsum())

customer_id = "CUS_0x5407"
# Belirli Customer_ID'ye bağlı değerleri filtreleyin
filtered_data = data[data['Customer_ID'] == customer_id]
print(filtered_data["Num_of_Delayed_Payment"])
# ############################ burada biter ################################

# ###################Num_Credit_Inquiries sütunumuzda bazı değişkenlerimiz problemliydi onu çözmeye çalıştık ###################
# burada num_of_loan değerleri type_of_loana göre düzenlencek type_of_loan leni kullanılabilir

customer_id = "CUS_0x21b1"
# Belirli Customer_ID'ye bağlı değerleri filtreleyin
filtered_data = data[data['Customer_ID'] == customer_id]
print(filtered_data["Num_Credit_Inquiries"])

data['Changed_Credit_Limit'] = data['Changed_Credit_Limit'].apply(lambda x: x.replace("_",""))

# 'Changed_Credit_Limit' sütunundaki değerlerde 2. noktadan sonrasını silme Saçma bir şey
data['Changed_Credit_Limit'] = data['Changed_Credit_Limit'].apply(lambda x: '.'.join(x.split('.')[:2]))

# Boş Occupation değerlerini Customer_ID'ye göre en yaygın değerle doldurma
data['Changed_Credit_Limit'] = data.groupby('Customer_ID')['Changed_Credit_Limit'].transform(lambda x: x.mode()[0])

# Belirli Customer_ID'ye bağlı değerleri filtreleyin
filtered_data = data[data['Customer_ID'] == customer_id]
print(filtered_data["Changed_Credit_Limit"])

# ############################ burada biter ################################

# ###################Num_Credit_Inquiries sütunumuzda bazı değişkenlerimiz problemliydi onu çözmeye çalıştık ###################
# burada num_of_loan değerleri type_of_loana göre düzenlencek type_of_loan leni kullanılabilir

customer_id = "CUS_0x21b1"
# Belirli Customer_ID'ye bağlı değerleri filtreleyin
filtered_data = data[data['Customer_ID'] == customer_id]
print(filtered_data["Num_Credit_Inquiries"])


is_float = data['Num_Credit_Inquiries'].apply(lambda x: isinstance(x, float)).all()
print(is_float)
# Boş Occupation değerlerini Customer_ID'ye göre en yaygın değerle doldurma
data['Num_Credit_Inquiries'] = data.groupby('Customer_ID')['Num_Credit_Inquiries'].transform(lambda x: x.fillna(x.mode()[0]))

# Belirli Customer_ID'ye bağlı değerleri filtreleyin
filtered_data = data[data['Customer_ID'] == customer_id]
print(filtered_data["Num_Credit_Inquiries"])

# ############################ burada biter ################################


# ###################Credit_Mix sütunumuzda bazı değişkenlerimiz problemliydi onu çözmeye çalıştık ###################
# burada num_of_loan değerleri type_of_loana göre düzenlencek type_of_loan leni kullanılabilir

customer_id = "CUS_0x21b1"
# Belirli Customer_ID'ye bağlı değerleri filtreleyin
filtered_data = data[data['Customer_ID'] == customer_id]
print(filtered_data["Credit_Mix"])


# Boş Occupation değerlerini Customer_ID'ye göre en yaygın değerle doldurma
data['Credit_Mix'] = data.groupby('Customer_ID')['Credit_Mix'].transform(lambda x: x.mode()[0])

# Belirli Customer_ID'ye bağlı değerleri filtreleyin
filtered_data = data[data['Customer_ID'] == customer_id]
print(filtered_data["Credit_Mix"])

# ############################ burada biter ################################

# ###################Outstanding_Debt sütunumuzda bazı değişkenlerimiz problemliydi onu çözmeye çalıştık ###################
# burada num_of_loan değerleri type_of_loana göre düzenlencek type_of_loan leni kullanılabilir

customer_id = "CUS_0x21b1"
# Belirli Customer_ID'ye bağlı değerleri filtreleyin
filtered_data = data[data['Customer_ID'] == customer_id]
print(filtered_data["Outstanding_Debt"])


# Boş Occupation değerlerini Customer_ID'ye göre en yaygın değerle doldurma
data['Outstanding_Debt'] = data.groupby('Customer_ID')['Outstanding_Debt'].transform(lambda x: x.mode()[0])

# Belirli Customer_ID'ye bağlı değerleri filtreleyin
filtered_data = data[data['Customer_ID'] == customer_id]
print(filtered_data["Outstanding_Debt"])

# ############################ burada biter ################################

# ###################Num_Credit_Inquiries sütunumuzda bazı değişkenlerimiz problemliydi onu çözmeye çalıştık ###################
# burada num_of_loan değerleri type_of_loana göre düzenlencek type_of_loan leni kullanılabilir

customer_id = "CUS_0x21b1"
# Belirli Customer_ID'ye bağlı değerleri filtreleyin
filtered_data = data[data['Customer_ID'] == customer_id]
print(filtered_data["Credit_Utilization_Ratio"])


is_float = data['Credit_Utilization_Ratio'].apply(lambda x: isinstance(x, float)).all()
print(is_float)

filtered_data = data[data['Customer_ID'] == customer_id]
print(filtered_data["Credit_Utilization_Ratio"])

# ############################ burada biter ################################


# ###################Num_Credit_Inquiries sütunumuzda bazı değişkenlerimiz problemliydi onu çözmeye çalıştık ###################
# burada num_of_loan değerleri type_of_loana göre düzenlencek type_of_loan leni kullanılabilir

customer_id = "CUS_0x21b1"
# Belirli Customer_ID'ye bağlı değerleri filtreleyin
filtered_data = data[data['Customer_ID'] == customer_id]
print(filtered_data["Credit_History_Age"])

# #######################
# hatalı sayılır bu satır
data['Credit_History_Age'] = data['Credit_History_Age'].apply(lambda x: "2 Years and 1 Months" if isinstance(x, float) else x)

data['Credit_History_Age'] = data.groupby('Customer_ID')['Credit_History_Age'].fillna(method='ffill')
data['Credit_History_Age'] = data.groupby('Customer_ID')['Credit_History_Age'].fillna(method='bfill')
data['Credit_History_Age'] = data['Credit_History_Age'].apply(lambda x: int(x.split()[0]) * 12 + int(x.split()[3]) )


filtered_data = data[data['Customer_ID'] == customer_id]
print(filtered_data["Credit_History_Age"])

# ############################ burada biter ################################

# ###################Total_EMI_per_month sütunumuzda bazı değişkenlerimiz problemliydi onu çözmeye çalıştık ###################
# burada num_of_loan değerleri type_of_loana göre düzenlencek type_of_loan leni kullanılabilir

customer_id = "CUS_0x21b1"
# Belirli Customer_ID'ye bağlı değerleri filtreleyin
filtered_data = data[data['Customer_ID'] == customer_id]
print(filtered_data["Total_EMI_per_month"])


# Boş Occupation değerlerini Customer_ID'ye göre en yaygın değerle doldurma
data['Total_EMI_per_month'] = data.groupby('Customer_ID')['Total_EMI_per_month'].transform(lambda x: x.mode()[0])

# Belirli Customer_ID'ye bağlı değerleri filtreleyin
filtered_data = data[data['Customer_ID'] == customer_id]
print(filtered_data["Total_EMI_per_month"])
# # ############################ burada biter ################################

# ###################Num_Credit_Inquiries sütunumuzda bazı değişkenlerimiz problemliydi onu çözmeye çalıştık ###################
# burada num_of_loan değerleri type_of_loana göre düzenlencek type_of_loan leni kullanılabilir

customer_id = "CUS_0x21b1"
# Belirli Customer_ID'ye bağlı değerleri filtreleyin
filtered_data = data[data['Customer_ID'] == customer_id]
print(filtered_data["Amount_invested_monthly"])

# #######################
# hatalı sayılır bu satır
data['Amount_invested_monthly'] = data['Amount_invested_monthly'].replace('__10000__', method='ffill',limit=1)
data['Amount_invested_monthly'] = data['Amount_invested_monthly'].replace('__10000__', method='bfill',limit=1)
data['Amount_invested_monthly'] = data.groupby('Customer_ID')['Amount_invested_monthly'].fillna(method='ffill')
data['Amount_invested_monthly'] = data.groupby('Customer_ID')['Amount_invested_monthly'].fillna(method='bfill')

data['Amount_invested_monthly'] = data['Amount_invested_monthly'].replace('0', method='ffill',limit=1)
data['Amount_invested_monthly'] = data['Amount_invested_monthly'].replace('0', method='bfill',limit=1)
filtered_data = data[data['Customer_ID'] == customer_id]
print(filtered_data["Amount_invested_monthly"])

# ############################ burada biter ################################

# ###################Num_Credit_Inquiries sütunumuzda bazı değişkenlerimiz problemliydi onu çözmeye çalıştık ###################
# burada num_of_loan değerleri type_of_loana göre düzenlencek type_of_loan leni kullanılabilir

customer_id = "CUS_0xd40"
# Belirli Customer_ID'ye bağlı değerleri filtreleyin
filtered_data = data[data['Customer_ID'] == customer_id]
print(filtered_data["Payment_Behaviour"])

# #######################
# hatalı sayılır bu satır
data['Payment_Behaviour'] = data['Payment_Behaviour'].replace('!@9#%8', method='ffill',limit=1)
data['Payment_Behaviour'] = data.groupby('Customer_ID')['Payment_Behaviour'].fillna(method='ffill')
data['Payment_Behaviour'] = data.groupby('Customer_ID')['Payment_Behaviour'].fillna(method='bfill')

filtered_data = data[data['Customer_ID'] == customer_id]
print(filtered_data["Payment_Behaviour"])

# ############################ burada biter ################################

# # ################### Monthly_Balance sütunumuzda bir problem varmı bunu anlamaya çalışıcaz ###################
# is_null = data['Monthly_Balance'].isnull().any()

# # Null değer varsa True, yoksa False döner
# print(is_null)

sütun_adı = 'Monthly_Balance'  # Kontrol etmek istediğiniz sütunun adını girin
data[sütun_adı] = data[sütun_adı].replace('__-333333333333333333333333333__', method='ffill')
data[sütun_adı] = data[sütun_adı].astype(float)

# Sütunda float olmayan bir sayı olup olmadığını kontrol etme
non_float_values = data[~data[sütun_adı].apply(lambda x: isinstance(x, float))]
if non_float_values.empty:
    print("Sütunda float olmayan bir sayı bulunmuyor.")
else:
    print("Sütunda float olmayan bir sayı bulunuyor.")
# # Non-integer ifadeleri içeren satırları yazdırmak
# print(len(non_integer_values) == 0)
# # çıktılarımıza bakar isek bir sıkıntı yok gibi
# # ############################ burada biter ################################
data.to_csv('veriler3.csv', index=False)