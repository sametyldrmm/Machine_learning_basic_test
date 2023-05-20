# Machine_learning_basic_test

# Proje Amacı Genel Bilgi
- ilk hedef olarak basit makine öğrenmesi projeleri geliştirmeye çalışıyorum amacım en basit örnekleri yaparak makine öğrenmesinin temmellerini öğrenmek
- Bu konu hakkındaki ilk çalışmam olduğunu belirtebilrim. Hiç bir şey bilmediğimi yazdığım şeylerin tamamen mantıksız olabileceğini kabul ediyor ve bu konuyla yeni ilgileniyorsanız yazacağım şeyleri kronolojik sırası ile inceleyeniz. Zaman içerisinde güncellenen bir repo olacaktır. Yazdıklarımın tamamen mantıksız olsa dahi yeni başlayanların düşeceği yanılgılar ve yanlışlarla dolu olabilir . Kronolojik sıra ile bu yanlışları tek tek belirteceğim. Böyle bir durumda yeni başlayanlar için belirli bir zaman sonra çok iyi bir kaynak olacağını düşünüyorum. 

# Modeller
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

# Yapılmış Uygulamalar
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

# Hedef Proje
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


## Güncellemeler
- İlk aşama için proje koşullarını basitleştirmeye karar verdim. Derin öğrenmeyi arka planda nasıl uygulayabileceğim konusunda henüz net bir fikrim yok.
- Mevcut durumda, hedefi rastgele alanlardan ziyade 400x400 sabit bir alana indirgedim.
- Sistem için öğrenebilmesi için veri oluşturmam gerekiyor ve daha sonra pekiştirmeli öğrenme modeliyle projeyi yeniden yapacağım. Veriyi giriş ve çıkışlara ayırmak gerekiyor.
### Sistem için Öğrenme Amaçlı Giriş ve Çıkışlar
  #### Girişler:
- Sistemin mevcut alanı anlayıp bu alandan sonuç döndürmesini sağlamak için alanı tamamını x-y çiftleri olarak sağlamaya karar verdim.
- Kabul noktalarının bağlanabileceği noktaların konumlarını sistemin anlayabilmesi için vermem gerekiyor.
- Giriş sayısını 10.000 olarak belirledim, yani alanda 10.000 farklı diziden oluşan her biri 10 rasgele sayı içeren diziler istiyorum.
- Giriş dizilerinin özellikleri:
- Tüm alan noktaları = [[x0, y0], [x0, y1], ...] (400x400 alan içindeki tüm noktalar)
- Bir rasgele nokta = [x0, y0]
- Bir girişin tüm rasgele noktaları = [bir rasgele nokta, ...]
- Bir giriş = tüm alan noktaları + bir girişin tüm rasgele noktaları
- Tüm girişler = [bir giriş, ...] (10.000 giriş)

#### Çıkışlar:
- Giriş sayısını 10.000 olarak belirlediğim için her bir giriş dizisi için bir çıkış dizisi olacak.
- Çıkış dizisinin özellikleri:
- Tek bir giriş için istenen çıkış = [puan, x koordinatı 0, y koordinatı 0]
- [tek bir giriş için istenen çıkış, ...] (10.000 çıkış)

Tahmini giriş ve çıkış verileri oluşturuldu.
Kodun C dilinde yazıldığını ve daha sonra ekleyeceğimi belirtmek istiyorum. Şu anda metin dosyalarını ekleyeceğim.

# Kaynaklar
- https://keras.io/api/models/
- https://keras.io/api/layers/
- https://chat.openai.com/ (verdiği bilgiler her zaman doğru mu diye kontrol edilir yada edilecektir. Çok sıkı bir şekilde kullanılır her zaman yorumdan uzak net bilgiler sorulmaya özen gösterilir)

# İletişim
Her zaman ilk başta ana kaynak olan Kerasın dökümanları kullanılmalı
Projelerde bana destek olup bu repoyu herkesin yararlanabileceği bir repo haline getirmek ve bana bu yolculuğumda yardım etmek isterseniz lütfen iletişime geçin

Gmail: yildirimsamet051@gmail.com


# ENGLISH 
# Project Purpose and General Information
- As a first goal, I am trying to develop simple machine learning projects to learn the basics of machine learning.
- I would like to mention that this is my first venture into this subject. I acknowledge that I know nothing, and what I write may be completely nonsensical.
- If you are new to this topic, please review what I write in chronological order. Over time, this repository will be updated.
- Although what I write may seem completely illogical, it may be filled with misconceptions and mistakes that beginners will encounter. In such a case, I believe it will be a valuable resource for beginners after a certain time. 

# Models
## The Sequential Model
This can be considered the simplest model I will encounter.
The main advantage of this model is its simplicity in implementation. For a model to be simple, it requires:
- Not having multiple input sources
- Not having multiple output targets
- Not reusing layers (reusability) in other models
If the input comes from a single source, the output goes to a single destination, and the layers are not used in other models, we can say that the model is simple.
!!!! Information taken from https://www.datasciencearth.com/keras-model-wars-sequential-vs-functional/

#### Functions to Use in Layers
- I will list them later.

#### General Structure
- Input layer
- Hidden layers
- Output layer

This is the general structure.

# Implemented Applications
## Number Prediction
Sequential model is used.
1 input, 1 output.
Creating a model using simple deep neural networks. It is a simple application where I try to predict numbers. In this application, what is observed is that reasonably accurate results can be obtained in simple linear data types. In my first attempt, when I trained the model with 1000 numbers between 0 and 100 and asked it to predict a number between 0 and 100, it could provide accurate results with an error margin below 0.1%.

## Predicting the Average of 2 Numbers
2 inputs, 1 output.
Sequential model is used.
It is built on top of the Number Prediction program and aims to demonstrate the difference in multidimensional inputs.

## 2 inputs, 2 outputs
- Since I'm just starting to work with layers, this kind of information is new to me. Normally, you don't do something like this in a Sequential model.
- I just want to show in a very simple way how to provide 2 inputs and 2 outputs.

# Target Project
The latest project I want to work on is connecting randomly scattered X target points to a minimum of Y acceptance points on a 3D plane.
In this project, I aim to use a reward system.
I want to emphasize that the code I wrote is a Naive algorithm. I aim to create a dataset using this algorithm. This code will be shared later. When the target project starts.

## Things I Don't Know
- What should I pay attention to when creating a model?
- What should I pay attention to when creating a dataset?
- Which algorithms can I use?
- If I want to use a pre-trained model, how can I find existing pre-trained models?
- There are many topics. Greetings to those who can admit that they know nothing :)
 
## Rules
- One acceptance point can connect to a maximum of 3 target points.
- An acceptance point can be connected to a target point if the distance between them is a maximum of 30.
- The shorter the distance between an acceptance point and a target point, the higher the score.
- Using fewer acceptance

## Updates
- I have decided to simplify the project's conditions for the initial stage. I am currently unsure of how to implement deep learning in the background.
- In the current state, the target has been reduced to a 2-dimensional plane with a fixed area of 400x400, instead of random areas.
- To proceed with deep learning, I need to generate data, which will then be used with a reinforcement learning model for the project. Data needs to be separated into inputs and outputs.
### Inputs and Outputs for the System to Learn
 #### Inputs:

- Since the goal is for the system to understand the existing area and return results from that area, I have decided to provide the entire area as x-y pairs.
- In order for the system to understand where the accept points can connect, I need to provide the locations of connectable points within the area.
- I have set the number of inputs to be 10,000, which means I want 10,000 different arrays of 10 random numbers within the area.
- Features of the input arrays:
- All area points = [[x0, y0], [x0, y1], ...] (all points within the 400x400 area)
- A random point = [x0, y0]
- All random points for an input = [random point, ...]
- An input = all area points + all random points for an input
- All inputs = [an input, ...] (10,000 inputs)
 #### Outputs:

- Since I have set the number of inputs to be 10,000, I will have one output array for each input array.
- Features of an output array:
- The desired output for a single input = [score, x coordinate 0, y coordinate 0]
- [desired output for a single input, ...] (10000 outputs)

Estimated input and output data have been generated.
I will mention that the code is written in C and will be added later. For now, I will include the text files.

# Resources
- https://keras.io/api/models/
- https://keras.io/api/layers/
- https://chat.openai.com/ (Information obtained from here should always be verified for accuracy. It is used rigorously and precise questions are asked, avoiding ambiguity.)
# Contact
Always start by referring to the official documentation of Keras.
If you would like to support the projects and help turn this repository into a resource that everyone can benefit from, please feel free to contact me.
Gmail: yildirimsamet051@gmail.com

