import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import save_model, load_model

# Eğitim veri setini oluşturma (örnek olarak kullanılan veriler)
X = []
for _ in range(1000):
    x1 = np.random.rand() * 100
    x2 = np.random.rand() * 100
    X.append([x1, x2])
X = np.array(X)

# Y değerlerini oluşturma
y = np.mean(X, axis=1)

# Veri kümesini normalize etme
X = X / 100
y = y / 100
# Derin sinir ağı modelini oluşturma ve eğitme
model =  load_model('sayi_ortalama')
model.add(Dense(64, activation='relu', input_dim=2))
model.add(Dense(64, activation='relu'))
model.add(Dense(1, activation='linear'))
model.compile(optimizer='adam', loss='mse')
model.fit(X, y, epochs=50, batch_size=32)

# Modeli kaydetme
save_model(model, 'sayi_ortalama')

def predict_number(number, model):
    normalized_numbers = np.array([[number[0] /100, number[1] / 100]])
    predicted_value = model.predict(normalized_numbers)[0]
    return predicted_value

# Test etme
test_number = [40,20]
prediction = predict_number(test_number,model)
print(f"Girilen sayı: {test_number}")
print(f"Tahmin edilen sayı: {prediction * 100}")
