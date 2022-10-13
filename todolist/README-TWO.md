#### Jelaskan perbedaan antara asynchronous programming dengan synchronous programming!
synchronus adalah pemrograman di mana kode dieksskusi secara berurutan dan ketika suatu kode dieksekusi, maka kode lain tidak dapat dieksekusi secara bersaman. Dalam synchromus programming, kita tidak bisa berinteraksi dengan halaman web ketika web sedang me-load sesuatu.
Lain halnya dengan asyncronus yang dapat mengeksekusi kode program secara bersamaan sehingga user dapat berinteraksi dengan web ketika web sedang me-load kode lain. Selain itu, halaman web tidak akan me-reload seluruh page ketika ada perubahan di sebagaian page

####  Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event-driven programming berarti suatu kode program dieksekusi berdasarkan event yang dilakukan oleh user, seprti klik button dan keypress. Salah satu penerapannya dalam tugas ini adalah pada menu create task yang mengunakan button dan letika diklik akan menampilkan modal form untuk membuat task baru.

####  Jelaskan penerapan asynchronous programming pada AJAX!
Ajax memungkinkan web untuk bekerja secara asyncronus dengan memproses request dari user di sisi background dalam bentuk xmlhttprequest.  Alhasil, aplikasi web yang menggunakan AJAX dapat mengirimkan dan menerima data dari server tanpa harus mereload keseluruhan halaman.

#### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas!
- buat sebuah function di views.py yang akan me-return response berupa json dan function add_task sama seperti function create_task
- tambahkan path(/json) dan path(add/) di urls.py
- buat script javascript di todilist.html. Baut function bernama reloadlist() untuk menampilkan seluruh task.Pada function tersebut, buat sebuah div card menggunakan template yang ada di boostrap dan isi card tersebut dengan menggunakan method get ajax dari function show_json di views.py yang telah dibuat sebelumnya. Pada button ganti status dan delete task, tambahkan event click, yamg mana ketika diklik, maka akan menjalankan function changt_task_status dan delete_task. Penambhan event dilakukan meggunakan method $. ajax dan jika succes, maka akan me-reload isi halaman secara asynchronus
- pada file yang sama, tambhakan script untuk membuat modal. Modal dibuta menggunakn template yang ada di boostrap. Kemudian, isi modal body dengan form, sama seperti di create.html. Kemudian, tambhakan event pada button submit meggunakan method submit jquery kemudian akan mengarhlan ke bagian add/ dan akan menjalankan function add_task untuk menyimpan data ke database. Jika sukse, reload halaman secara asyncronus menggunakan method reloadlist()








