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
- lakukan git add . ,lalu git commit, dan git push ke github.


