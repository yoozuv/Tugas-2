## http://tugas2-app.herokuapp.com/katalog/

![request-respones](https://github.com/yoozuv/Tugas-2/blob/main/katalog/Tugas%202%20PBP.drawio.png)

### 2.Jelaskan kenapa menggunakan virtual environment?<br> Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Virtual environtment digunakan untuk mengisolasi package dan dependencies aplikasi sehingga tidak bertabrakan dengan versi lain yang ada pada komputer. Dengan menggunkan virtual environtment, kita dapat menggunkan modul dengan versi yang berbeda dengan modul yang terinstall secara global di komputer. Tanpa menggunakan virtual environtmen pun, kita masih bisa membuat apliaksi django<br><br>
### 3.Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.<br>
  1.import models ke file views.py. Models digunakan untuk mengambil data dari database. Kemudian buat function show_katalog dengan parameter request. Fungsi ini akan mengembalikan HTTP response. dalam fungsi ini, kita juga memebuat query dengan nama variable context yang akan di-masukkan sebagai parameter fungsi render. hal ini bertujuan agar data pada variabel context di-render oleh Django dan dikembalikan pada sebuah HTML.
  
  ```python
from django.shortcuts import render 

from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    data_catalog_items = CatalogItem.objects.all()
    context = {
        'catalog_items': data_catalog_items,
        'nama': 'Yoozu'
    }
    return render(request, "katalog.html",context)

``` 

2. lakukan routing pada file urls.py. Kita harus import fungsi show_katalog pada viewspy terlebih dahulu, lalu tambahkan url pattern
```
from django.urls import path
from katalog.views import show_katalog

app_name = 'katalog'

urlpatterns = [
    path('', show_katalog, name='show_katalog')
]
```
Kemudian, daftarkan aplikasi `katalog` pada `urls.py` yang ada di folder `project_django` dengan cara menambahkan potongan kode berikut pada variabel `urlpatterns`.
```
path('katalog/', include('katalog.urls')),
```

3. bukalah file `katalog.html` di folder `templates` dan isi bagian nama menggunakan sintaks django, yaitu {{data}}.
<h5>Name: </h5>
<p>{{nama}}</p>

```

Untuk menampilkan items pada tabel, lakukan iterasi pada `catalog_items` yang berada di dalam variabel `context` dan memanggil atribut dari objek

{% for item in catalog_items %}
    <tr>
        <th>{{item.item_name}}</th>
        <th>{{item.item_price}}</th>
        <th>{{item.item_stock}}</th>
        <th>{{item.description}}</th>
        <th>{{item.rating}}</th>
        <th><a href="{{item.item_url}}">{{item.item_url}}</a></th>
    </tr>
{% endfor %}
```
4. Buatlah sebuah app baru di website Heroku, lalu bukalah repositori GitHub dan pergi ke `Settings -> Secrets -> Actions -> New repository secret`. Lalu isi field `Name` dengan `HEROKU_APP_NAME` dan field `Secret` dengan nama app yang sudah dibuat `tugas2-app`. Buatlah secret baru satu lagi yang bernama `HEROKU_API_KEY` dan isi dengan key yang ada di  `Account settings` pada profile Heroku.




