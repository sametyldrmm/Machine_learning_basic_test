# Credit score prediction app

Bu projedeki amacımız deep learning kullanarak kredi score larını tahmin etmeye çalışacağız.

- Veri temizleme 
- Model oluşturma

Adımlarından oluşacaktır.

## 1) Veri Temizleme (Data Cleaning)

Bu adımda, veri setindeki eksik veya hatalı verileri düzeltecek veya çıkaracak işlemler gerçekleştirilir. Aşağıdaki yöntemleri kullanabilirsiniz:
- Eksik verilerin doldurulması
- Aykırı değerlerin ele alınması
- Gürültülü verilerin düzeltilmesi

### 1.1) Veri Dönüşümü (Data Transformation)

Bu adımda, veri setindeki özelliklerin dönüştürülmesi veya dönüşüm işlemleri uygulanması yapılır. Aşağıdaki yöntemleri kullanabilirsiniz:
- Sayısal olmayan kategorik verilerin sayısal forma dönüştürülmesi
- Tarih/saat verilerinin uygun formata dönüştürülmesi

#### 1.1.1) İstatistiksel olarak değerli sütunlar

Bu alt adımda, veri setindeki istatistiksel olarak değerli sütunları belirleyerek bu sütunlar üzerinde özel işlemler yapabilirsiniz. Bu sütunları belirlemek için özellik seçimi yöntemlerini kullanabilirsiniz.

#### 1.1.2) İstatistiksel olarak değersiz sütunlar

Bu alt adımda, veri setindeki istatistiksel olarak değersiz sütunları belirleyerek bu sütunları çıkarabilir veya dönüştürebilirsiniz. Bu şekilde, model performansını artırabilirsiniz.

Bu şekilde bir aşama yapıcak olmamızın ana sebebi bu sefer modeli kurgularken farklı bir yöntem denemek istemem. aslında 1 model değil 2 model oluşturacağım ve önemli görülen verilere daha çok dikat çekerek bu 2 modeli tek bir modelde birleştirerek işleyeceğim.
Ensemble Modelleri ve Bagging   adı altında geçen şeylerdir. Çok detaylı bir bilgiye sahip olmadığım konulardandır.

### 1.3) Veri Normalizasyonu (Data Normalization)

Bu adımda, veri setindeki değerleri belirli bir aralığa veya ölçeğe dönüştürme işlemleri yapılır. Aşağıdaki yöntemleri kullanabilirsiniz:
- Özellik değerlerini 0 ile 1 arasında ölçeklendirme
- Z-skor standardizasyonu gibi yöntemler

### 1.4) Özellik Seçimi (Feature Selection)

Bu adımda, veri setindeki özelliklerin seçilmesi veya azaltılması işlemleri yapılır. Aşağıdaki yöntemleri kullanabilirsiniz:
- İnformasyon kazancı, korelasyon analizi veya model tabanlı seçim gibi yöntemler

### 1.5) Veri Bölümleme (Data Partitioning)

Bu adımda, veri seti eğitim, doğrulama ve test kümelerine bölünür. Bu bölme işlemi, modelin eğitiminde kullanılacak veri kümesini belirlemek ve modelin performansını değerlendirmek için yapılır.


Buradaki sıraya uyulmasada buradaki her bir adım yapılmaya çalışılcaktır.

# Model oluşturma

**Not:** O noktaya gelindiğinde eklenecektir.



**Not:** Şuan sistem yönetimi ile ilgilendiğim için uzun bir süre güncelleme gelmeyecek bir konudur.
