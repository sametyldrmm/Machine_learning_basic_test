# Machine_learning_basic_test

# Informations
- ilk hedef olarak basit makine öğrenmesi projeleri geliştirmeye çalışıyorum amacım en basit örnekleri yaparak makine öğrenmesinin temmellerini öğrenmek
- Bu konu hakkındaki ilk çalışmam olduğunu belirtebilrim. Hiç bir şey bilmediğimi yazdığım şeylerin tamamen mantıksız olabileceğini kabul ediyor ve bu konuyla yeni ilgileniyorsanız yazacağım şeyleri kronolojik sırası ile inceleyeniz. Zaman içerisinde güncellenen bir repo olacaktır. Yazdıklarımın tamamen mantıksız olsa dahi yeni başlayanların düşeceği yanılgılar ve yanlışlarla dolu olabilir . Kronolojik sıra ile bu yanlışları tek tek belirteceğim. Böyle bir durumda yeni başlayanlar için belirli bir zaman sonra çok iyi bir kaynak olacağını düşünüyorum. 

# Models
## The Sequential model
Karşılaşacağım en basit model denilebilir.
Olayı gayet basit bir şekilde kurgulanabilir olmasıdır.
Bu model çeşidinde modelin implementasyonu basittir. Bir modelin basit olması için:
- Birden farklı input kaynağının olmaması
- Çoklu output hedeflerine sahip olmaması
- Katmanları tekrar tekrar kullanmaması (reusability)
Gerekir. Buna göre bir modelin inputu tek bir yerden geliyorsa, outputu tek bir yere gidiyorsa, katmanlar başka modellerde kullanılmıyorsa o model basittir diyebiliriz.
!!!! https://www.datasciencearth.com/keras-model-wars-sequential-vs-functional/ sitesinden alınan bilgiler
#### Katmanlarda kullanabileceğimiz fonksiyonlar
- belirli bir zaman sonra listeleyeceğim
#### Genel yapı
- Input layer
- Hidden layers
- Output layer
Genel yapı bu şekilde oluşur

# Done Project
## Sayi tahmini
Sequantial model kullanılmıştır
1 input 1 output
Basit bir derin sinir ağları kullanan bir model oluşturmak. Sayı tahmin ettirmeye çalıştığım basit bir uygulama . Bu uygulamada görülen şey basit bir doğrusal veri çeşitlerinde başarılı denebilecek seviyede sonuçlar elde edilebilior ilk denememde 0 ile 100 arasındaki 1000 sayı ile modeli eğittiğimde 0 ile 100 arasındaki bir sayıyı tahmin etmesini istediğimde bana yüzde 0.1 in altındaki hata payı ile doğru çıktıları verebiliyor.
## 2 Sayının ortalamasını tahmin ettirme
2 input 1 output
Sequantial model kullanılmıştır
Sayi tahimini programının üzerine inşa edilmiş olup çok boyutlu inputlarda nasıl bir farklılık olduğunu göstermeyi amaçlar.
## 2 input 2 output
- Layerlarla daha ilk kez çalıştığım için bu gibi bilgiler benim için yeni. Normalde Sequantial modelde böyle bir şey yapmazsınız
- Çok basit bir şekilde tek göstermek istediğim 2 input ve 2 output nasıl verilir.

# Target Project
En son yapmak istediğim proje. 3 Boyutlu bir düzlemde rasgele dağılmış X hedef noktaya minumum Y kabul noktası kullanarak birbirine bağlamak.
Bu projede ödül sistemi kullanmayı hedeflemekteyim.
Anlatacağım projeyi normal cpp kodu ile yapmış olduğumun altını çizmek isterim. Bu yazdığım kod Naive bir algoritma kullanır durumda bu algoritma ile bir veri seti oluşturmayı hedefliyorum. Bu kod daha sonra paylaşıcaktır. Hedef projeye başlandığı zaman.

## Bilmediklerim
- Bir model oluştururken nelere dikat etmeliyim.
- Bir veri seti oluşturuken nelere dikat etmeliyim.
- Hangi algoritmaları kullanabilirim.
- Hazır model kullanmak istersem var olan hazır modelleri nasıl bulabilrim ?
- Çok fazla başlık var. Hiç bir şey bilmediğini kabul edebilenlere selam olsun :)
 ## Kurallar
- Bir kabul noktası en fazla 3 hedef noktaya bağlanabilir.
- Bir kabul noktası bir hedef noktası ile aralarındaki mesafe maksimum 30 ise bağlanabilir
- Bir kabul noktası ile bağlanabileceği bir hedef noktası arasındaki mesafe ne kadar kısa ise o kadar yüksek bir puana sahip olacaktır.
- Daha az kabul noktası kullanmak her zaman daha yüksek puana sahip olacaktır.

### Kaynaklar
- https://keras.io/api/models/
- https://keras.io/api/layers/
- https://chat.openai.com/ (verdiği bilgiler her zaman doğru mu diye kontrol edilir yada edilecektir. Çok sıkı bir şekilde kullanılır her zaman yorumdan uzak net bilgiler sorulmaya özen gösterilir)

Her zaman ilk başta ana kaynak olan Kerasın dökümanları kullanılmalı
Projelerde bana destek olup bu repoyu herkesin yararlanabileceği bir repo haline getirmek ve bana bu yolculuğumda yardım etmek isterseniz lütfen iletişime geçin
Gmail: yildirimsamet051@gmail.com
