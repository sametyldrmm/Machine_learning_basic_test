import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import save_model, load_model

# Eğitim veri setini oluşturma (örnek olarak kullanılan veriler)
X = np.random.rand(1000, 1) * 100
y = X    # Gerçek değerlere olan uzaklıklar


# Veri kümesini normalize etme
X = X / 100
y = y / 100
# Derin sinir ağı modelini oluşturma ve eğitme
model = load_model('sayi_tahmin_modeli2')
model.add(Dense(64, activation='relu', input_dim=1))
model.add(Dense(64, activation='relu'))
model.add(Dense(1, activation='linear'))
model.compile(optimizer='adam', loss='mse')
model.fit(X, y, epochs=50, batch_size=32)

# Modeli kaydetme
save_model(model, 'sayi_tahmin_modeli2')

def predict_number(number):
    normalized_number = number / 100
    predicted_value = model.predict(np.array([normalized_number]))[0][0]
    return predicted_value

# Test etme
test_number = 88
prediction = predict_number(test_number)
print(f"Girilen sayı: {test_number}")
print(f"Tahmin edilen sayı: {prediction * 100}")
