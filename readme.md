BİBO CHATBOT README

Bu proje, bir chatbot uygulamasıdır. Aşağıda, projenin kullanımı, kurulumu ve gerekli kütüphaneler hakkında bilgiler bulunmaktadır.

Kurulum
Bu projeyi çalıştırmak için öncelikle bir sanal ortam oluşturmanızı öneririm. Sanal ortam, projenin bağımlılıklarını izole etmek için kullanılır. Sanal ortam oluşturmak için aşağıdaki komutu çalıştırabilirsiniz:

python -m venv myenv

Sanal ortamı etkinleştirin:

venv\Scripts\activate

Gerekli kütüphaneleri yüklemek için aşağıdaki komutu çalıştırın:

pip install -r requirements.txt
Proje klasöründe, aşağıdaki komutu kullanarak Flask uygulamasını başlatın:


python run.py
Flask uygulaması başarıyla başlatıldıktan sonra, http://localhost:5000 adresine erişerek chatbot uygulamasını kullanabilirsiniz.

Kullanım
Ana sayfaya erişmek için http://localhost:5000 adresine gidin.
admin Paneli için http://localhost:5000/admin adresine gidin
Makaleleri görüntülemek için http://localhost:5000/articles adresine gidin.
Belirli bir makaleye ait ayrıntıları görüntülemek için http://localhost:5000/article-detail/<id> adresine gidin, <id> yerine makale ID'sini ekleyin.
Gerekli Kütüphaneler
Proje, aşağıdaki kütüphaneleri kullanır:

Flask: Web uygulamaları oluşturmak için kullanılan bir mikro web çerçevesi.
Flask SQLAchemy: Flask ile SQL veritabanlarıyla etkileşim için kullanılan bir eklenti.
Flask Admin: Flask uygulamaları için yönetici paneli oluşturmayı sağlayan bir eklenti.
NLTK: Doğal dil işleme (Natural Language Processing - NLP) işlemleri için kullanılan bir kütüphane.
Keras: Derin öğrenme modelleri oluşturmak için kullanılan bir kütüphane.
Yukarıdaki kütüphaneleri requirements.txt dosyasında bulabilirsiniz.
![yeşilay](https://github.com/biboemre/BiboChatbotApp/assets/97239219/a0497e89-d13f-4eb4-942f-7ce43395685e)
