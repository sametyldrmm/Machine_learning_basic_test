import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import save_model, load_model
from sklearn.preprocessing import MinMaxScaler
import numpy as np
# CSV dosyasını okuma
data = pd.read_csv('common.csv')
data = data.drop('ID', axis=1)


print(data.dtypes)