link heroku http://tugas2-app.herokuapp.com/todolist/ <br>
1.csrf_token merupakan perlindungan yang dilakukan django terhadap serangan Cross Site Request Forgery. Token csrf merupakan token  yang digunakan untuk mencegah serangan Cross Site Request Forgery. csrf_token memberikan token unik untuk setiap session pengguna.
token ini bersifat random dan unik. Dengan menggunkan csrf_token, pihak yang tidak memiiki token ini tidak bisa melakukan suatu operasi/tindakan/request di form, seperti memasukkan link yang mengarah ke website tertentu atau dapat menghapus data.
Jika tidak menggunakan csrf_token, maka pada form dapat dilaukan serangan CSRF seperti yang dicontohkan tadi. 
<br>
2. Bisa, caranya buat  file form.py. Lalu buat sebuah class dan beri atribut/ field dari form sesuai yang diperlukan. Kemudian buat sebuah fungsi di views.py untuk memproses form. Pada fungsi tersebut, buat sebuah instance dari class form. Validasi form tersebut. Jika valid, save form tersebut. Selanjutnya buat dictionary bernama context, lalu isi cntext dengan instace dari class for yang telah dibuat sebelumnya.  return reder(request,'form.html',context). Setelah itu, buat file form.html di folder template. isi form.html dengan <form> dan tambhakan field yang diperlukan. Isi field tersebut dengan data dari context dengan menggunakan syntax {{namainstace.namafield}}. Lalu tambahka tag <button> dengan type submit.
<br>
3. User mengisi form dan men-submit. kemudian, data dikirimkan menggunakan method POST melalui HTTP request dan diproses oleh method di views.py. Jika data yang di-submit valid, maka data disimpan ke database. Selanjutnya, data tersebut ditampilkan dalam bentuk HTML dengan memasukkan data tersebut ke variabel context. Lalu, fungsi yang ada di views.py  ini akan me-render data tersebut untuk dimasukkan ke file HTML.
  <br>
4.
- Buat apliaksi baru menggunakan comand python manage.pr startapp todolist. lalu, tambahakan 'todolist' ke list installed_apps di settings.py
- Buat sebuah class bernama Task di folder models. Pada class tersebut, tambahkan atribut yang dibutuhkan, yaitu user,date,title, description.
- tambahka fungsi  register, login_user, dan logout_user di views.py seperti yang dilakukan di lab 3.
- tambhakan fungsi show_todolist di views.py untuk menampilka todolist user 
- buat folder templates, lalu buat file login.html,register.html, dan todlist.html sama sperti lab 3.
- tambahkan urlpatern di urls.py sesuai dengan ketentuan soal
- buat file form.py yang digunakan unuk membuat form create task. Pada file ini, buat sebuah class bernama TaskForm dan tambahka atribut title dan description.
- buat fungsi create_task di views.py. Fungsi ini diguka untuk memproses data yang di-submit melalui form create task.
- buat file create.html untuk mengambil input user
- tambhkan urlspattern untu create task di urls.py sesi dengan ketentuan soal
- daftarkan url todolist di urlspattern padafile urls.py folder project_django
- tambhakan fungsi change_task_status dan delete_task di views.py untuk mengubah STATUS TASK DAN MENGHAPUS TAKS
- tambahkan urlpattern di urls.py sesuai dengan ketentuan soal
- lakukan migration data menggunkan comand python manage.py makemigrations dan pyton manage.py migrate 
- lakukan git add . ,lalu git commit, dan git push ke github
 
### Tugas 5
  
1. #### Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
  - inline : styling css secara langsung di dalam tag yang akan di-styling, <p style=......>. Dengan menggunakan inline css, kita dapat melakukan styling untuk element secara langsung sehingga tidak ememakan banyak waktu. Selain itu, proses permintaan HTTP lebih kecil sehingga proses load website akan lebih cepat. Tetapi, metode ini tidak efisien karena stiap style hanya berlaku untuk satu element saja
  - internal : styling dilakukan di dalam tag <style> yang berada di file yang sama dengan dengan file HTML. Kelebihan internal css antara lain,
   Perubahan hanya terjadi pada 1 halaman, Class dan ID bisa digunakan oleh internal stylesheet, Tidak perlu meng-upload beberapa file karena HTML dan CSS bisa digunakan di file yang sama. Kekurangannya yaitu tidak efisien jika akan menggunakan style yang sama untuk beberapa halaman.
  - eksternal : styling dilakukan di file lain. CSS ditulis di sebuah file khusus yang berekstensi .css dan biasanya diletakkan setelah bagian <head> pada halaman.
  Kelebihan dari ekstenal css antara lain ukuran file HTML akan menjadi lebih kecil, struktur dari kode HTML jadi lebih rapi, dan File CSS  tersebut dapat digunakan di beberapa halaman/ file HTML sekaligus.
  
2. #### Jelaskan tag HTML5 yang kamu ketahui.
  - `<table>` : digunakan untuk membuat tabel. Di dalam tag ini, kita dapat menambahkan <th>,<tr>,<td>.
  - `<a>` : digunakan untuk menambahkan hyperlink.
  - `<h1>-<h6>` : mendefinisikan heading. Teridir dari h1-h6.
  - `<input>`   : digunakan untuk meminta input user. Tag ini memeiliki beberapa type, seperti text,date,submit, dan password.
3. #### Jelaskan tipe-tipe CSS selector yang kamu ketahui.
  - class : digunakan untuk ememilih element berdasarkan class yang diberikan. Selector ini dibuat dengan menambahkan "." sebelum nama clasa.
  - id    : memilih element berdasarkan id. Dibuta dengan menambahkan "#" sebelum id yang akan dipilih.
  - tag   : memilih element bardasarkan tag yang digunakan.

 4. #### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
  - incude boostrap ke base.html dengan menambahkan  `<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">` di bagian head dan  `<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>` di agian body.
  - styling element pada halaman login, create, register, dan todolist dengan menggunakan code  yang ada di dokumentasi boostrap.
  - kustomisasi halaman todolist dengan menggunakan menggunakan <div class="card mb-3" style="width: 30%; margin:auto">
  
