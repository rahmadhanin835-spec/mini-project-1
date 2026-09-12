# mini-project-1

pada kode diatas, terdapat antrian dan nomor_antrian. kode antrian merupakan list kosong yang akan menjadi database sementara untuk menyimpan semua antrean pelanggan. setiap antrian disimpan sebagai tuple. lalu kode nomor_antrian merupakan variabel penghitung, dimulai dari satu yang akan terus bertambah setiap ada antrean baru yang ditambahkan.

kode while true membuat program terus berjalan dalam bentuk perulangan sampai ada perintah break (menu 4). setiap perulangan, menu dicetak ulang, lalu program menungu input pilihan dari user(string "1","2" di variabel pilih. 

saat user memilih "1", program akan meminta nama pelanggan, lalu menampilkan daftar 3 jenis layanan. layanan tersebut akan menyimpan pilihan user(string)

conditional statement tersebut akan memetakan pilihan angka ketiga variabel: nama layanan, harga, dan estimasi waktu
jika input tidak sesuai, ia akan masuk ke else yang akan menampilkan  error, lalu continue membuat program kembali ke awal while true lagi. hal tersebut akan mencegah program melanjutkan proses data yang tidak lengkap

input nilai yang dimasukkan akan dicek apakah <= 0. kalau iya, akan diangap tidak valid.

semua data pelanggan akan digabung jadi satu tuple data dengan urutan tetap. kode antrian.append(data) akan menambahkan tuple ke dalam list antrian

nomor_antrian berfungsi untuk menaikkan penghtungan agar antrean berikutnya mendapatkan nomor sesudah nomor sebelumnya

if not antrian: mengecek apakah list antrian kosong. kalau kosong, kode akan menampilkasn pesan. kalau ada isinya, program akan melakukan pengulangan. for data in antrian: seriap data adalah satu tuple antrean, lalu mencetak isinya satu persatu mengggunakan index tuple 

list akan dicek terlebih dahulu, apakah list kosong. proram akan mencari tuple denhan data[0] yang cocok sesuai input. jika ketemu, akan dihapus dengan .remove(data) lalu break dan keluar dari loop for

break disini menghentikan while true dipaling luar, sehingga program akan berakhir. namun, ada kasus kalau user mengetik menu selain "1" - "4", akan menambilpkan pesan "pilihan menu tidak tersedia"
