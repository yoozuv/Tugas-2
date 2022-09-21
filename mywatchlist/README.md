## 1. Link  App Tugas 3 <br>
http://tugas2-app.herokuapp.com/mywatchlist/html/ <br>
http://tugas2-app.herokuapp.com/mywatchlist/xml/ <br>
http://tugas2-app.herokuapp.com/mywatchlist/json/ <br>

## 2. Postman
<br> <br>
### HTML
![request-respones](https://github.com/yoozuv/Tugas-2/blob/main/mywatchlist/postman1.png)
<br>
### xml
![request-respones](https://github.com/yoozuv/Tugas-2/blob/main/mywatchlist/postman2.png)
<br>
### json
![request-respones](https://github.com/yoozuv/Tugas-2/blob/main/mywatchlist/postman3.png)

### 3. A. perbedaan antara JSON, XML, dan HTML
HTML merupakan markup language yang digunakan untuk membentuk struktur tampilan dari suatu web, sedangkan 
XML  merupaka markup language yang digunakan dalam menyimpan dan tranport data dan
json merupakan format peyimpanan dan transport data yang diperlukan oleh web. 
Jadi, HTML berkaitan dengan  tampilan (penyajian) data yang dibutuhkan user di halaman web, sedangkan xml dan json berkaitan dengan penyimpanan dan transport data 
### B. mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Implemetasi data delivery dilakukan agar platform dapat menampilkan  data yang dibutuhkan oleh user dan megolah data yang diberikan user secara tepat

### C.

- Buat aplikasi baru : `python manage.py startapp mywatchlist` dan tambahkan ke list `INSTALLED_APPS` di settings.py
- Buka models.py kemudian buat class MyWatchlistItem dan tambhakan atribut yang diperlukan, yaitu title, wathced,rating,review,release_date
- Lakukan perintah `python manage.py makemigrations` lalu Jalankan perintah `python manage.py migrate` untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.
- Buat sebuah folder bernama fixtures di dalam folder aplikasi `mywatchlist` dan buatlah sebuah berkas bernama `data_watchlist.json` yang berisi 10 data film.
- Jalankan perintah `python manage.py loaddata data_watchlist.json` untuk memasukkan data tersebut ke dalam database Django lokal.
- Buka views.py yang ada pada folder mywatchlist. Pada views.py, buat query `data_mywatchlist_items`. Kemudian buat fungsi `show_mywatchlist` yang menerima parameter request. Di dalam fungsi tersebut, buat sebuah dictionary bernama context yang berisi key watchlist_items,nama,NPM. Fungsi ini kemudian akan men-return `render(request, "mywatclist.html",context)`.
- Kemudian buat juga fungsi show_xml yang akan mengembalikan `HttpResponse(serializers.serialize("xml", data_mywatchlist_items), content_type="application/xml")` dan show_json yang akan mengembalikan `HttpResponse(serializers.serialize("json", data_mywatchlist_items), content_type="application/json")`
- Buatlah sebuah folder bernama templates di dalam folder aplikasi mywatchlist dan buatlah sebuah berkas bernama `mywatchlist.html` . File html ini akan menapilkan data dari film yang ada di data_watchlist.json
- Buatlah sebuah berkas di dalam folder aplikasi `mywatchlist` bernama `urls.py` untuk melakukan routing terhadap fungsi views yang  dibuat sehingga nantinya halaman HTML dapat ditampilkan lewat browser. 

``` from django.urls import path
from mywatchlist.views import show_json, show_mywatchlist, show_xml

app_name = 'mywatchlist'

urlpatterns = [
    
    path('html/',show_mywatchlist , name='show_mywatchlist'),
    path('xml/',show_xml , name='show_xml'),
    path('json/',show_json , name='show_json'),

  ]```.

```
- tambahkan urlspattern di urls.py dengan `path('mywatchlist/',include('mywatchlist.urls')),`
- Buat unit test untuk memeriksa respons aplikasi.
- Sesuaikan `Procfile` dengan menambahkan `loaddata data_watchlist.json` .
- *Add*, *commit*, dan *push* ke github. Kemudian, GitHub Actions akan men-*deploy* aplikasi ke Heroku




