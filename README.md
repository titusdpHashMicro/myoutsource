# myoutsource

## Deskripsi My Outsource

My Outsource merupakan suatu sistem untuk perusahaan penyedia pegawai outsource. Pada sistem ini ada beberapa object yang memiliki keterkaitan yaitu :
- **Pegawai Outsource** <br/>Pegawai dari luar perusahaan inti yang terdaftar pada pegawai outsource yang siap disalurkan ke perusahaan mitra
- **Pegawai Internal** <br/>Pegawai dari dalam perusahaan inti yang terdaftar sebagai pekerja internal.
- **Supervisor** <br/>Pekerja yang berada di mitra yang menjadi supervisor dari pegawai outsource.
- **Mitra** <br/>Perusahaan yang sudah melakukan kerja sama dengan perusahaan inti dimana jika sewaktu waktu membutuhkan tenaga kerja maka perusahaan inti bisa menyalurkan pegawai outsource untuk bekerja di mitra
- **Fasilitas** <br/>Fasilitas yang disediakan oleh perusahaan inti untuk pegawai internal
- **Peminjaman** <br/>Datar riwayat peminjaman terhadap fasilitas yang dilakukan oleh pegawai internal
## Fitur secara garis besar
1. Chatter (tracking, schedule, dan message)
2. Wizard (create new record)
3. Export PDF
4. Compute field
5. Sequence
6. Order via model
7. dan materi yang diajarkan dikelas lainnya
## Penjelasan fitur pada My Outsource
*Setiap object yang baru di buat sudah dibuatkan sequence yang otomastis berbeda dengan data yang sudah ada serta tiap tabel memiliki prefix yang berbeda*
### Menu yang tersedia
1. Pegawai
   #### Sub menu :
   1. Pegawai Outsource
      - Memiliki bentuk form dan tree
      - Model merupakan inheritance dari myoutsource.pegawai
      - Data yang ditampilkan di filter berdasarkan domain is_outsource = True
      - Memiliki status bar yang merupakan status pegawai tersebut, antara lain : Waiting (Menunggu panggilan untuk pekerjaan), Contract (Dalam fase administrasi dengan perusahaan mitra {field mitra harus terisi}), On Work (Sudah bekerja di mitra {field supervisor dan gaji harus terisi}), Done (Sudah selesai bekerja di suatu mitra {field mitra dan supervisor otomatis dikosongkan}), Quit (Sudah tidak terdaftar sebagai pegawai outsource)
      - Memiliki chatter yang berfungsi sebagai pesan, tracking perubahan field dan siapa yang mengubahnya.
      - supervisor sudah di filter berdasarkan
   2. Pegawai Internal
      - Memiliki bentuk form dan tree
      - Data yang ditampilkan di filter berdasarkan domain is_internal = True
      - Dapat melakukan peminjaman fasilitas dan memiliki relasi many-to-one dengan peminjaman
      - Memiliki chatter yang berfungsi sebagai pesan, tracking perubahan field dan siapa yang mengubahnya.<br><br>

2. Supervisor <br>
    - Memiliki relasi many-to-one dengan mitra dan memiliki relasi one-to-many dengan pegawai outsource <br>
    - Terdapat fungsi untuk menghitung total pegawai yang diawasinya<br><br>
3. Mitra
    - Memiliki relasi one-to-many dengan pegawai outsource (hanya bagi pegawai yang memiliki status 'On Work') dan supervisor
    - Memiliki fungsi yang menghitung total_gaji yang harus dibayarkan tiap bulan berdasarkan jumlah pegawai dan gajinya
    - Memiliki fungsi yang menghitung total pegawai outsource yang bekerja di mitra
    - Bisa di export ke pdf dengan template yang sudah ditentukan serta nama file yang sudah disesuaikan pada masing masing mitra<br><br>
4. Fasilitas
    - Memiliki relasi one-to-many dengan pegawai internal (hanya yang dengan status peminjaman 'On Progress')<br><br>
5. Peminjaman
    - Memiliki relasi many-to-one dengan pegawai internal dan fasilitas
    - Memiliki status bar yang memiliki fungsi tersendiri, antara lain Draft (masih bersifat sementara dan belum di acc), On Progress (Fasilitas sedang digunakan dan dilakukan pengecekkan stok serta tanggal peminjaman), Done (fasilitas sudah dikembalikan dan ada pengecekkan terkait tanggal pengembalian) 
    - Dapat menyesuaikan jumlah stok sehingga apabila semua fasilitas sedang digunakan maka pegawai yang lain tidak akan bisa menggunakan fasilitas tersebut
    - Pada menu 'Peminjaman' terdapat child yang bernama 'Create Peminjaman' dimana berfungsi untuk membuat record baru pada peminjaman tetapi menggunakan wizard
    - Memiliki chatter yang berfungsi sebagai pesan, tracking perubahan field dan siapa yang mengubahnya.<br><br>