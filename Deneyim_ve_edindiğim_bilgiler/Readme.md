## Aktivasyon Fonksiyonları
### ReLU (Rectified Linear Unit):
ReLU, negatif değerleri sıfıra eşitlerken, pozitif değerleri aynen bırakan basit bir aktivasyon fonksiyonudur.
Genellikle derin sinir ağlarında kullanılır.
Sıfır olmayan gradyanlara sahiptir ve hesaplama açısından hızlıdır.


### Sigmoid:
Sigmoid, giriş değerini [0, 1] aralığına sıkıştıran bir aktivasyon fonksiyonudur.
Binary sınıflandırma problemlerinde (örneğin, lojistik regresyon) ve ara katmanlarda kullanılabilir.
Sigmoid, herhangi bir girişe karşı daha yumuşak ve yavaş bir yanıt verirken, sınırlarda doygunlaşma eğilimi gösterir.

### Softmax:
Softmax, çok sınıflı sınıflandırma problemlerinde kullanılan bir aktivasyon fonksiyonudur.
Çoklu sınıf çıktılarını olasılık dağılımlarına dönüştürür, böylece her sınıfın olasılığını temsil eder.
Softmax çıktıları birbirleriyle karşılaştırılabilir ve toplamı 1'e eşittir.


### Softplus:
Softplus, giriş değerini sıfırdan başlayarak sınırsız bir aralığa genişleten bir aktivasyon fonksiyonudur.
Yumuşak bir eğriye sahiptir ve ReLU'ya benzer bir davranış sergiler.
Negatif girişlere karşılık sıfıra yaklaşırken, pozitif girişlere doğrusal bir şekilde artar.

### Softsign:
Softsign, giriş değerini [-1, 1] aralığına sıkıştıran bir aktivasyon fonksiyonudur.
Softsign, sigmoid fonksiyonuna benzer bir şekilde girişin sınırlara yaklaşırken doygunlaşma eğilimi gösterir.
ReLU'dan farklı olarak, softsign herhangi bir değere karşılık gelebilen bir çıkış üretebilir.
Tanh (Hiperbolik Tanjant):


### Tanh, giriş değerini [-1, 1] aralığına sıkıştıran bir aktivasyon fonksiyonudur.
Sigmoid fonksiyonuna benzerdir, ancak sigmoid sıfıra yaklaştıkça doygunlaşırken, tanh simetrik olarak doygunlaşır.
Ara katmanlarda sıklıkla kullanılır ve çıkış aralığının merkezini sıfır yaparak ağırlıklı bir çıktı


### Selu:
Selu (Scaled Exponential Linear Unit), otomatik normalleştirme özelliğine sahip bir aktivasyon fonksiyonudur.
Derin sinir ağlarında stabiliteyi artırmak için kullanılır.
Selu, negatif değerlerde eğilimli olarak 1.0507 ile çarpılarak genişlerken, pozitif değerlerde lineer bir davranış sergiler.
Bu aktivasyon fonksiyonu, ağın kendisini ayarlamasına yardımcı olabilir ve aşırı uyumu azaltabilir.

### Elu (Exponential Linear Unit):
Elu, negatif değerlerde lineer olmayan bir yanıt verirken, pozitif değerlere doğrusal bir yanıt veren bir aktivasyon fonksiyonudur.
Negatif girişlerde daha yumuşak bir eğime sahiptir ve ReLU'dan farklı olarak doygunlaşma problemini hafifletir.
ReLU'nun dezavantajı olan "ölü nöron" sorununu azaltabilir.

### Exponential:
Exponential, giriş değerinin üstel bir fonksiyonunu hesaplayan bir aktivasyon fonksiyonudur.
Pozitif girişler için yüksek değerler üretirken, negatif girişler için yaklaşık olarak sıfıra yaklaşır.
Genellikle özel durumlarda kullanılır ve doğrusal olmayan bir çıkış elde etmek için kullanılabilir.


## Tahmin İnceleme Yöntemleri

Model tahmini ve gerçek değer arasındaki farkı istatistiksel olarak değerlendirmek için aşağıdaki yöntemler kullanılabilir:

- **Ortalama Mutlak Hata (Mean Absolute Error, MAE):** Prediction ve gerçek değer arasındaki mutlak farkların ortalamasını hesaplar. Daha düşük bir MAE değeri, tahminin gerçek değere daha yakın olduğunu gösterir.

- **Ortalama Kare Hatası (Mean Squared Error, MSE):** Prediction ve gerçek değer arasındaki farkların karelerinin ortalamasını hesaplar. MSE, daha yüksek hataları daha fazla vurgulayan MAE'ye göre daha hassas bir metriktir.

- **Kök Ortalama Kare Hatası (Root Mean Squared Error, RMSE):** MSE'nin karekökünü alarak elde edilir. Gerçek değerlerin ölçeğine daha uygun bir ölçüdür ve MSE ile aynı birimde ifade edilir.

- **R-Kare (R-Squared):** Gerçek değerlerin varyansının tahmin edilen değerler tarafından açıklanan oranını ifade eder. 1'e yaklaşan bir R-kare değeri, tahminin gerçek değeri daha iyi açıkladığını gösterir.

Bu metriklerin yanı sıra, hata dağılımını görselleştirmek için grafikler ve histogramlar kullanılabilir. Ayrıca, hata analizi için istatistiksel testler de uygulanabilir.

## Optimizasyon Algoritmaları

Optimizasyon algoritmaları, yapay sinir ağlarının eğitimi sırasında kullanılan yöntemlerdir. İşte yaygın olarak kullanılan bazı optimizasyon algoritmaları:

- **Gradient Descent (GD):** En temel optimizasyon algoritmasıdır. Gradientin (eğim) negatif yönünde ağırlıkları güncelleyerek kaybı azaltır. Farklı varyasyonları bulunur.

- **Stochastic Gradient Descent (SGD):** Eğitim verilerinin küçük gruplarını (batch) kullanarak gradienti hesaplar ve ağırlıkları günceller.

- **Mini-batch Gradient Descent:** SGD ve tam batch GD arasında bir orta noktadır. Belirli bir batch boyutunda eğitim verilerini kullanır.

- **Adaptive Moment Estimation (Adam):** SGD'nin bir varyasyonudur ve yaygın olarak kullanılan bir optimizasyon algoritmasıdır. Adaptive learning rate (uyumlu öğrenme oranı) kullanır ve her parametrenin kendi adaptif öğrenme oranına sahip olmasını sağlar.

- **RMSProp:** Root Mean Square Propagation olarak da bilinir. Gradientin karesinin hareketli ortalamasını kullanarak adaptif bir öğrenme oranı sağlar.

- **AdaGrad:** Daha önceki gradyanların karesinin toplamını kullanarak adaptif öğrenme oranı sağlar.

- **AdaDelta:** AdaGrad'in bir genişlemesi olarak kullanılan bir optimizasyon algoritmasıdır.

- **Adamax:** Adam'ın bir genişlemesidir. Büyük gradyanları kontrol etmek için maksimum normu kullanır.

- **Nadam:** Adam ve Nesterov Momentum'un bir kombinasyonudur.

Bu optimizasyon algoritmaları, modelin kaybını (loss) en aza indirmek için ağırlıkların güncellenmesini sağlar.

## Aşırı Uyumu Önleme Yöntemleri

Aşırı uyumu önlemek için aşağıdaki yöntemler kullanılabilir:

- **Daha fazla veri toplamak:** Daha büyük ve çeşitli veri setleri, modelin genelleştirme yeteneğini artırabilir ve aşırı uyumu azaltabilir.

- **Veri ön işleme:** Veri ön işleme adımları, gürültüyü azaltmak, aykırı değerleri ele almak ve dengesizlikleri düzeltmek için kullanılabilir.

- **Daha basit bir model kullanmak:** Modelin karmaşıklığını azaltarak aşırı uyumu azaltabilirsiniz.

- **Regularizasyon teknikleri:** L1 ve L2 düzenlileştirme, dropout ve early stopping gibi teknikler kullanarak aşırı uyumu azaltabilirsiniz.

- **Çapraz doğrulama yapmak:** Veri setini eğitim, doğrulama ve test kümelerine ayırarak modelin genelleştirme performansını objektif bir şekilde değerlendirebilirsiniz.

Bu yöntemler, aşırı uyumu azaltmak için kullanılan yaygın tekniklerdir.

## Veri Kalitesi ve Ön İşleme

- Veri setinizin kalitesi çok önemlidir. Veri setindeki gürültülerin, eksik değerlerin veya aykırı değerlerin olabileceği durumları kontrol etmek ve bu durumlarla başa çıkmak için veri ön işleme adımlarını uygulamak önemlidir.

- Veri setini analiz edin ve gereksiz veya anlamsız özellikleri belirleyin. Doğru özellik seçimi, modelin karmaşıklığını azaltabilir ve aşırı uyumu önleyebilir.

- Veri setinde eksik değerler varsa, bu değerleri doldurmak veya eksik değerleri içeren örnekleri kaldırmak için uygun yöntemleri kullanın.

- Aykırı değerleri tespit edin ve bunlarla başa çıkmak için uygun yöntemleri uygulayın. Aykırı değerlerin veri setinizin genel dağılımını etkilemediğinden emin olun.

## Model Hiperparametreleri ve Optimizasyon

- Modelin hiperparametrelerini optimize etmek, modelin performansını artırmak için önemlidir. Hiperparametreler arasında ağaç sayısı, maksimum derinlik, öğrenme oranı, regulasyon terimleri gibi değerler bulunabilir.

- Grid Search, Rastgele Arama veya Bayesian yöntemler gibi hiperparametre ayarlama tekniklerini kullanarak en iyi hiperparametre kombinasyonunu bulun.

- Modelinizi daha hızlı ve daha iyi sonuçlar elde etmek için en son optimizasyon algoritmaları ile eğitin. Örnek olarak, Adam, RMSProp veya SGD gibi optimizasyon algoritmalarını kullanabilirsiniz.

- Early stopping gibi teknikleri kullanarak aşırı uyumu önleyin. Eğitim sürecini izleyerek, modelin performansının artık gelişmediği bir noktada eğitimi durdurabilirsiniz.

## Ensemble Modelleri ve Bagging

- Ensemble (birleşik) modeller, birden fazla modelin tahminlerini birleştirerek daha iyi bir performans elde etmenizi sağlar. Örneğin, Rastgele Ormanlar veya Gradient Boosting gibi ensemble yöntemleri kullanabilirsiniz.

- Bagging yöntemlerini kullanarak modelin kararlılığını artırabilirsiniz. Bootstrapping yöntemiyle birden fazla örneklem oluşturarak her örnekleme üzerinde ayrı ağaç modelleri eğitin ve sonuçları birleştirin.

## Veri Büyütme (Data Augmentation) ve Regularizasyon

- Veri setinizi çeşitlendirmek ve genişletmek için veri büyütme tekniklerini kullanmak modelin genelleştirme yeteneğini artırabilir. Örneğin, görüntü verileri için resim döndürme, kesme veya yansıtma gibi yöntemler kullanabilirsiniz.

- Regularizasyon tekniklerini kullanarak aşırı uyumu önleyin. Örneğin, L1 veya L2 düzenlileştirme gibi düzenleme terimlerini ekleyebilir veya dropout gibi düşürme yöntemlerini kullanabilirsiniz.

## Model Doğrulama ve Değerlendirme

- Doğru bir model doğrulama stratejisi kullanmak, modelin genelleştirme yeteneğini değerlendirmek ve aşırı uyumu kontrol etmek için önemlidir.

- K-fold çapraz doğrulama veya zaman serisi veri setleri için geçerli doğrulama yöntemlerini kullanarak modelinizi değerlendirin.

- Metrikleri (örneğin, doğruluk, hassasiyet, geri çağırma, F1 puanı) değerlendirin ve modelinizi bu metriklerle karşılaştırın.

## Regresyon Problemleri ve Kullanılan Yöntemler

Regresyon problemleri, bağımlı bir değişkenin (çıktı) bağımsız değişkenlere (girişler) bağlı olarak sürekli değerler aldığı problemleri ifade eder. Aşağıda bazı regresyon problemleri ve kullanılan yöntemlerin örnekleri bulunmaktadır:

1. Ev Fiyat Tahmini:
   - Ev fiyatlarının tahmin edilmesi gibi problemlerdir.
   - Lineer regresyon, çoklu regresyon, karar ağaçları, destek vektör regresyonu (SVR), rastgele ormanlar, gradient boosting gibi yöntemler kullanılabilir.

2. Gelir Tahmini:
   - Kişilerin gelir düzeylerinin tahmin edilmesi gibi problemlerdir.
   - Lineer regresyon, polinom regresyonu, destek vektör regresyonu (SVR), yapay sinir ağları (MLP), gradient boosting yöntemleri kullanılabilir.

3. Satış Tahmini:
   - Ürün satışlarının tahmin edilmesi gibi problemlerdir.
   - Zaman serisi analizi, ARIMA modelleri, otoregresif entegre hareketli ortalama (ARIMA), holt-winters yöntemleri, yapay sinir ağları gibi yöntemler kullanılabilir.

4. Hastalık Prognozu:
   - Hastalığın ilerlemesi veya hastanın sağlık durumunun tahmin edilmesi gibi problemlerdir.
   - Cox regresyonu, survival analizi, yapay sinir ağları (MLP), destek vektör regresyonu (SVR), rastgele ormanlar, gradient boosting yöntemleri kullanılabilir.

5. Maliyet Tahmini:
   - Bir projenin veya işin maliyetinin tahmin edilmesi gibi problemlerdir.
   - Lineer regresyon, çoklu regresyon, rastgele ormanlar, destek vektör regresyonu (SVR), gradient boosting gibi yöntemler kullanılabilir.

Bu sadece regresyon problemlerine örnekler ve kullanılan yöntemlere genel bir bakıştır. Her problemin kendine özgü gereksinimleri ve veri seti özellikleri bulunur, bu nedenle doğru yöntemi seçmek önemlidir.


## Batch Size ve Model Eğitimi

Batch_size, bir eğitim iterasyonunda kullanılan örnek sayısını belirleyen bir parametredir. Eğitim veri seti genellikle büyük miktarda örnek içerir ve bu örnekleri aynı anda modelinize beslemek verimlilik açısından mümkün olmayabilir. Bu durumda, eğitim veri setini daha küçük gruplara, yani batch'lere ayırmak faydalı olur.

Batch_size değeri, eğitim esnasında aynı anda işlenen örneklerin sayısını belirler. Örneklerin gruplara bölünüp işlenmesi, bellek kullanımını optimize eder ve işlem süresini hızlandırır. Büyük bir veri setinde, daha küçük batch'ler kullanmak, GPU veya TPU gibi hızlandırıcıları daha etkin bir şekilde kullanmanıza olanak sağlar.

Yüksek batch_size, daha fazla örneği aynı anda işlemenizi sağlar ve bu da eğitim süresini kısaltabilir. Ancak, yüksek batch_size değeri bellek gereksinimini artırır ve daha az ayrıntılı güncellemeler yapılmasına neden olabilir. Ayrıca, genellemeyi iyileştirmek için daha küçük batch'lerin tercih edildiği bazı durumlar vardır.

Batch_size değeri, modelinizi ve kullanılabilir kaynakları (bellek, GPU vb.) göz önünde bulundurarak deneme yanılma yoluyla belirlenmelidir. Farklı batch_size değerlerini deneyerek modelin performansını ve eğitim süresini izleyebilir ve ihtiyaçlarınıza en uygun değeri bulabilirsiniz.

## Kategorik Veri Dönüştürme Yöntemleri

Kategorik verilerin sayısal değerlere dönüştürülmesi için farklı yöntemler bulunmaktadır. İşte bazı yaygın kullanılan yöntemler:

1. Etiket Kodlama (Label Encoding):
   - Bu yöntemde, kategorik veriler sıralı bir şekilde sayısal etiketlere dönüştürülür.
   - Her kategoriye benzersiz bir sayı atanır.
   - Örneğin, "Kırmızı", "Mavi", "Yeşil" gibi kategoriler 0, 1, 2 gibi sayılara dönüştürülebilir.
   - Bu yöntemle dönüştürülen veriler, kategori sıralaması gibi yanlış anlamlar içerebilir.

2. One-Hot Kodlama (One-Hot Encoding):
   - Bu yöntemde, her kategori için yeni bir özellik oluşturulur ve sadece ilgili kategoriye ait özellik 1, diğerleri 0 değerini alır.
   - Bu şekilde, her kategori benzersiz bir sayısal vektöre dönüştürülür.
   - Örneğin, "Kırmızı", "Mavi", "Yeşil" gibi kategoriler için [1, 0, 0], [0, 1, 0], [0, 0, 1] gibi vektörler oluşturulabilir.
   - Bu yöntemle her bir kategori arasında eşit mesafeler oluşturulur, ancak veri boyutu artabilir.

3. Ordinal Kodlama (Ordinal Encoding):
   - Bu yöntemde, kategorik veriler sıralanabilir bir mantıkla sayısal değerlere dönüştürülür.
   - Her kategoriye bir sayı atanır ve bu sayılar kategoriler arasında bir sıralamayı yansıtır.
   - Örneğin, "Kötü", "Orta", "İyi" gibi kategoriler -1, 0, 1 gibi sayılara dönüştürülebilir.
   - Bu yöntemle sıralama bilgisi korunur, ancak aralıklar arasında eşit mesafeler varsayılmaz.

4. Binary Encoding:
   - Bu yöntemde, kategorik veriler, her bir kategori için birer bitin kullanıldığı bir sayısal temsil ile kodlanır.
   - Her kategoriye benzersiz bir sayı atanır ve bu sayılar ikilik sistemde temsil edilir.
   - Örneğin, "Kırmızı", "Mavi", "Yeşil" gibi kategoriler 0, 1, 2 gibi sayılara dönüştürülerek ikilik sistemde temsil edilebilir (0: 00, 1: 01, 2: 10).
   - Bu yöntemle veri boyutu kontrol altında tutulur ve kategorik bilgiler korunur.

Bu yöntemlerden hangisini kullanacağınız, verilerinizin özelliklerine ve analiz amacınıza bağlıdır. Genellikle, One-Hot Encoding yaygın olarak tercih edilen bir yöntemdir.


## Model Değerlendirme Metrikleri

Birkaç farklı model değerlendirme metriği bulunmaktadır. İşte bazı yaygın kullanılan metrikler:

1. Doğruluk (Accuracy):
   - Sınıflandırma problemlerinde yaygın olarak kullanılan bir metrik olan doğruluk, doğru tahminlerin toplam veri noktalarına oranını temsil eder.
   - Yüzde olarak ifade edilir ve 1'e ne kadar yakınsa, modelin o kadar iyi performans gösterdiği anlamına gelir.

2. Kayıp (Loss):
   - Kayıp metriği, modelin tahminlerinin gerçek değerlerden ne kadar uzak olduğunu ölçer.
   - Kayıp değeri ne kadar düşükse, modelin o kadar iyi performans gösterdiği anlamına gelir.
   - Farklı problemler için farklı kayıp fonksiyonları kullanılabilir, örneğin ortalama karesel hata (MSE) veya ikili çapraz entropi (binary cross-entropy).

3. Hassasiyet (Precision) ve Geri Çağırma (Recall):
   - Hassasiyet, modelin pozitif olarak tahmin ettiği örneklerin gerçek pozitiflerin yüzdesini ölçer.
   - Geri çağırma, gerçek pozitiflerin ne kadarının doğru bir şekilde tahmin edildiğini ölçer.
   - Sınıf dengesizlikleri olan problemlerde, hassasiyet ve geri çağırma gibi sınıf bazlı metrikler daha bilgilendirici olabilir.

4. F1-Skoru (F1-Score):
   - Hassasiyet ve geri çağırma arasında bir denge sağlayan F1-skoru, bu iki metriğin harmonik ortalamasını temsil eder.
   - Sınıf dengesizlikleri olan problemlerde, doğruluk yerine F1-skoru kullanmak daha uygun olabilir.

5. AUC-ROC (Alan Altındaki Eğri):
   - Sınıflandırma problemlerinde kullanılan bir başka değerlendirme metriği olan AUC-ROC, modelin duyarlılık ve özgüllük performansını gösteren bir eğri altındaki alanı temsil eder.
   - AUC-ROC değeri ne kadar yüksekse, modelin o kadar iyi performans gösterdiği anlamına gelir.

6. Ortalama Mutlak Hata (MAE) ve Ortalama Kare Hatası (MSE):
   - Regresyon problemlerinde kullanılan değerlendirme metrikleridir.
   - MAE, gerçek ve tahmin edilen değerler arasındaki mutlak farkların ortalamasını temsil eder.
   - MSE, gerçek ve tahmin edilen değerler arasındaki kare farkların ortalamasını temsil eder.

 ## Layer Tasarımı İçin Dikkat Edilmesi Gereken Faktörler

1. Veri seti ve problem alanı:
   İlk olarak, çalıştığınız veri setini ve çözmek istediğiniz problem alanını anlamanız önemlidir. Veri setinizin boyutu, özellikleri, dağılımı ve problem alanının gereksinimleri, layerların tasarımını etkileyen faktörlerdir. Örneğin, görüntü işleme problemleri için konvolüsyonel katmanlar tercih edilirken, doğal dil işleme problemleri için rekürsif veya dikkat katmanları kullanılabilir.

2. Modelin karmaşıklığı:
   Modelin karmaşıklığı, veri setinin karmaşıklığı ve problem alanının gereksinimleri ile uyumlu olmalıdır. Daha karmaşık bir model, daha fazla öğrenme kapasitesi ve esneklik sağlayabilir, ancak aşırı uyumaya neden olabilir. Modeli karmaşıklaştırmak, aynı zamanda eğitim süresini ve hesaplama maliyetini artırabilir. Bu nedenle, modelin yeterince karmaşık olduğundan emin olmalı, aşırı uyumaya dikkat etmeli ve gereksinimlerinizi karşılayacak düzeyde olmalıdır.

3. Layer sayısı ve boyutu: 
   Modelin layer sayısı ve boyutu, modelin öğrenme kapasitesini ve genelleme yeteneğini etkiler. Daha fazla layer, modelin daha karmaşık özellikler öğrenmesini sağlayabilir, ancak aşırı uyum riskini artırır. Layer boyutları, girdi boyutu ve çıktı boyutu arasında denge sağlamalıdır. Giriş boyutunu çok hızlı bir şekilde daraltmak veya genişletmek yerine, adım adım özellik çıkarımını ve karmaşıklığı artırmak daha iyidir.

4. Aktivasyon fonksiyonları:
   Her layerda kullanılan aktivasyon fonksiyonları, modelin öğrenme sürecini ve genelleme yeteneğini etkiler. Örneğin, girişlerin sınırlarını geçici olarak kaldırmak için ReLU (Rectified Linear Unit) yaygın olarak kullanılırken, sigmoid veya tanh fonksiyonları daha sınırlı bir çıktı aralığı sağlar. Aktivasyon fonksiyonlarının doğru seçimi, modelin öğrenme sürecini hızlandırabilir ve daha iyi sonuçlar elde etmenizi sağlayabilir.

5. Aşırı uydurma (overfitting):
   Aşırı uydurma, modelin eğitim verilerine çok iyi uyması ancak genelleme yeteneğinin düşük olması durumudur. Aşırı uydurmayı önlemek için dropout, düzenlileştirme (regularization) ve erken durdurma (early stopping) gibi yöntemler

## Layer katmanındaki seçenekler

1. Dense Layer :
- "Dense" terimi, derin öğrenme (deep learning) alanında yaygın olarak kullanılan bir terimdir. "Dense" ağ katmanı, tam bağlantılı bir yapının olduğu ve tüm giriş birimlerinin tüm çıkış birimlerine bağlandığı bir yapının bir örneğidir. Bu katman, her bir giriş birimini her bir çıkış birimiyle bağlar ve her bir bağlantının ağırlığı optimize edilir.
- "Dense" katmanı, yapay sinir ağlarının yaygın bir bileşenidir ve genellikle ileri besleme sinir ağlarının (feedforward neural networks) bir parçası olarak kullanılır. Bu katman, verileri doğrudan bir katmandan diğerine iletmek için kullanılır. Önceki katmandaki her birim, bu katmandaki her bir birimle bağlantılıdır ve her bir bağlantıda bir ağırlık vardır.
- "Dense" katmanı, ağın çıktılarını oluşturmak için girdi özelliklerini kullanır. Her bir giriş birimi, ağırlıklarıyla çarpılır ve ardından bir aktivasyon fonksiyonundan geçirilir. Bu, her bir çıkış birimine bir ağırlık atanmasını ve sonuçların hesaplanmasını sağlar.

Derin öğrenme modellerinde "Dense" katmanları, genellikle birbiri ardına sıralanarak kullanılır. Bu, birbirini takip eden katmanların birbiriyle tam bağlantılı olduğu bir yapı oluşturur. Her bir katmanın çıkışı, bir sonraki katmanın girişi haline gelir. Bu şekilde, modelin daha karmaşık özellikler ve ilişkiler öğrenmesi sağlanır.
"Dense" terimi, başka bir yaygın terim olan "fully connected" ile de eşanlamlıdır. Bu, her bir giriş biriminin her bir çıkış birimiyle bağlantılı olduğu anlamına gelir.

bazı alternatifler:

2. Convolutional Layer (Konvolüsyonel Katman): 
  - Görüntü işleme alanında yaygın olarak kullanılan bu katman, girdi veri üzerinde konvolüsyon işlemlerini uygular. Bu katman, özellik haritalarını öğrenmek için kullanılır ve görüntüdeki lokal bağıntıları yakalamak için etkili bir şekilde çalışır.

Recurrent Layer (Tekrarlayan Katman): 
  - Seri veya zamanla değişen verileri işlemek için kullanılan bir katmandır. Önceki adımların çıktılarını hatırlar ve zamanla ilişkili bilgiyi tutabilir. LSTM (Long Short-Term Memory) ve GRU (Gated Recurrent Unit) gibi tekrarlayan katman türleri sıklıkla kullanılır.

Pooling Layer (Havuzlama Katmanı): 
  - Girdi verinin boyutunu azaltmak ve özelliklerin ölçeklendirilmesini sağlamak için kullanılan bir katmandır. Max pooling veya average pooling gibi işlemlerle, bir bölgenin en büyük veya ortalama değeri alınarak boyut azaltılır.

Dropout Layer (Atıştırmalık Katmanı):
  - Aşırı uydurmayı (overfitting) önlemek için kullanılan bir katmandır. Rastgele birimleri belli bir olasılıkla atarak, modelin aşırı uyumlu olmasını engelleyebilir.

Batch Normalization Layer (Grup Normalleştirme Katmanı): 
  - Eğitim sırasında ağın içerisindeki her bir katmandaki girdi değerlerini normalleştiren bir katmandır. Bu, eğitim sürecini hızlandırabilir ve daha iyi sonuçlar elde etmeyi sağlayabilir.

Attention Layer (Dikkat Katmanı): 
  - Özellikle doğal dil işleme ve çeviri gibi görevlerde kullanılan bir katmandır. Dikkat mekanizması, modelin belirli kısımlarına odaklanmasını sağlar ve önemli bilgilere daha fazla ağırlık verir.

Bu, sadece bazı örneklerdir ve daha birçok farklı katman türü ve yapılandırma mevcuttur. Modelinize uygun olan katmanları seçmek, veri türüne, soruna ve hedefe bağlıdır.
