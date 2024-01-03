buttonElement.addEventListener('click', () => {
  const inputValue = inputElement.value.trim(); // Boşlukları kaldır

  if (inputValue === '') {
    // Giriş boşsa veya yalnızca boşluklar içeriyorsa uyarıyı gösterin
    alertElement.style.display = 'block';
  } else {
    // Yeni öğeyi liste ekleyin
    // ...

    // Uyarıyı gizleyin
    alertElement.style.display = 'none';

    // Metin alanını sıfırlayın
    inputElement.value = '';
  }
});
Yeni Öğe Ekleme: "Ekle" düğmesine tıklandığında yeni bir öğe eklemeniz gerekiyor. Bu işlemi "Ekle" düğmesine bir olay dinleyici ekleyerek ve giriş alanındaki değeri kontrol ederek gerçekleştirebilirsiniz.
javascript
Copy code
// DOM'dan gerekli elementleri alın
const inputElement = document.getElementById('input');
const buttonElement = document.getElementById('button');
const listElement = document.getElementById('list');

// "Ekle" düğmesine tıklanınca yeni öğeyi ekleyin
buttonElement.addEventListener('click', () => {
  const inputValue = inputElement.value.trim(); // Boşlukları kaldır

  if (inputValue !== '') {
    // Yeni öğeyi liste ekleyin
    // ...

    // Metin alanını sıfırlayın
    inputElement.value = '';

    // Uyarıyı gizleyin
    alertElement.style.display = 'none';
  } else {
    // Giriş boşsa veya yalnızca boşluklar içeriyorsa uyarıyı gösterin
    alertElement.style.display = 'block';
  }
});
DOM'dan Uyarı Kutusu Kaldırma: Bir öğe eklediğinizde uyarı kutusunu DOM'dan kaldırmamız gerekiyor. Bu, uyarı elementine "display: none" stilini ekleyerek yapılabilir.
javascript
Copy code
// Yeni öğe eklenirse uyarıyı gizleyin
alertElement.style.display = 'none';
Yeni Öğe Eklendiğinde Metin Alanı Sıfırlama: Bir öğe eklediğinizde, metin alanının içeriğini sıfırlamanız gerekiyor. Bunun için inputElement.value'yi boş bir dize olarak ayarlayabilirsiniz.
javascript
Copy code
// Metin alanını sıfırlayın
inputElement.value = '';
Her Üçüncü Öğeyi Kırmızı Yapma: Her üçüncü öğeyi kırmızı yapmalısınız. Bunun için liste içindeki öğelerin sayısını sayabilir ve her üçüncü öğeyi kırmızı yapabilirsiniz.
javascript
Copy code
// Her üçüncü öğeyi kırmızı yap
if (listElement.children.length % 3 === 2) {
  listItem.style.color = 'red';
} else {
  listItem.style.color = 'black';
}
Bu adımları takip ederek, belirtilen gereksinimlere uygun bir JavaScript uygulaması oluşturabilirsiniz. Bu kodu projenizin src/js/script.js dosyasına eklemeniz gerekecektir.





